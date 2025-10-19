```json
{
  "id": "c4ba7b52f2ee3c68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287695,
  "host_pid": "9e6742732c60:1",
  "hash": "2ef3daf0d1d22cce47f47d27e57f79511bc09b8be196d85925628ce6fde1474b",
  "cid": "QmV12ef3daf0d1d22cce47f47d27e57f79511bc09b8b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287695,
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
      "evaluated_at": 1760287695
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
  "sig": "28f78c7e376149e0b55c005b0c0e9832462c8fe4208366b6ccb9873040826d35"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 111000020703113
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 19840467, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285763, 'matching_hash': '6c2ac9b0cec56c2f'}}}