```json
{
  "id": "fceb6638e2bfaee8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293833,
  "host_pid": "9e6742732c60:1",
  "hash": "010325ab785ade4b0bf65a0810daea2c8549cbdce1fdab21e38fa171587aca88",
  "cid": "QmV1010325ab785ade4b0bf65a0810daea2c8549cbdc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293833,
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
      "evaluated_at": 1760293833
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
  "sig": "d5247b8ae3ec3914299d6151a2fb89e1df1381490e145905cf6681f90b937ca8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029964192
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 68569530, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285764, 'matching_hash': '3fa9c762fe00e5a2'}}}