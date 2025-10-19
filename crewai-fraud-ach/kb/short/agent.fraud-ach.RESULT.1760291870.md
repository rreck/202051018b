```json
{
  "id": "16a72e3d226a081e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291870,
  "host_pid": "9e6742732c60:1",
  "hash": "c53678a5d091c225ee29fcc8ac0006db3601b54d1d5451359af897ba9261bc54",
  "cid": "QmV1c53678a5d091c225ee29fcc8ac0006db3601b54d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291870,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760291870
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "e8a3a917bfa7fc2da7799a70f4386ceae5915d8ac1494707f55016d568bb1aa8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465523405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 54146355, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285764, 'matching_hash': '5adc701fe9b49cb3'}}}