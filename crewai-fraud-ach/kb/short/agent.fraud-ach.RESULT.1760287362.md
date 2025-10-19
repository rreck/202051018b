```json
{
  "id": "b89dc8b3e1e4ece3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287362,
  "host_pid": "9e6742732c60:1",
  "hash": "cd863e44ff0429b4cd71fdc43340643a09f4f7b3c39ed92268fcaa12f02d8575",
  "cid": "QmV1cd863e44ff0429b4cd71fdc43340643a09f4f7b3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287362,
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
      "evaluated_at": 1760287362
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "b6427f6a17e13d8f26a6175caf2df3af6b861f420658b9e948f11703989f8cea"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000021865843
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 14250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285765, 'matching_hash': '0e7cb19dffe9e37d'}}}