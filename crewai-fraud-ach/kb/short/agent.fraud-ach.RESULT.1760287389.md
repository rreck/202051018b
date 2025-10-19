```json
{
  "id": "becffaab44674c5b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287389,
  "host_pid": "9e6742732c60:1",
  "hash": "bc4f52de218b48ca9105fe7b6063ec007598151924876d25829c7ce008324002",
  "cid": "QmV1bc4f52de218b48ca9105fe7b6063ec0075981519",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287389,
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
      "evaluated_at": 1760287389
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
  "sig": "a3774e5bfbfbe8138a29267051774594c80420f88859e5dfb7ee7c188ea66c24"
}
```

Fraud detected: duplicate_transaction (score: 75)
Transaction: 044000034020503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 66, 'details': {'transaction_count': 58, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285765, 'matching_hash': '8db66b2beb557931'}}}