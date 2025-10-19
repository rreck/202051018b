```json
{
  "id": "ff392ae4d2470c5c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293075,
  "host_pid": "9e6742732c60:1",
  "hash": "a90c57d8bb3d6929fc9f3726b7e4ca505d0adea88287af46342c8f62b16eca04",
  "cid": "QmV1a90c57d8bb3d6929fc9f3726b7e4ca505d0adea8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293075,
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
      "evaluated_at": 1760293075
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
  "sig": "7ef887da433db8db8b171de927f11e3292884c8e2978f10de8d17afe3b71e3fb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245124241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 68664253, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285764, 'matching_hash': '1e6f1dd53bdf6417'}}}}