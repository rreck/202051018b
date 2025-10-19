```json
{
  "id": "3cec975d6a018bd2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293270,
  "host_pid": "9e6742732c60:1",
  "hash": "d34eaca9714adac16bad976e70cb717b7c4ad9dd02a72de2e8e88b69ae4c2900",
  "cid": "QmV1d34eaca9714adac16bad976e70cb717b7c4ad9dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293270,
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
      "evaluated_at": 1760293270
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
  "sig": "c9d7b5ab280e93aecfc6908775f6643c143c892c11f21af2c69bb23144a46520"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026701294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 55395395, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285764, 'matching_hash': 'c6488d75609f0f90'}}}