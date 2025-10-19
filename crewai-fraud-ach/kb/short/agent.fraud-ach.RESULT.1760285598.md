```json
{
  "id": "752ac590ae883136",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285598,
  "host_pid": "9e6742732c60:1",
  "hash": "b6b2e22477ca52c0e437ad593e50f5741150f0b2c1f3518d9de3bd02caa8a5e8",
  "cid": "QmV1b6b2e22477ca52c0e437ad593e50f5741150f0b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285598,
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
      "evaluated_at": 1760285598
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
  "sig": "66ca52ebc0c5ff1cba8f403737d07486f989edfbadc21553ad2f90ed5d326765"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 25705034, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}