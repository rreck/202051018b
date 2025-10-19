```json
{
  "id": "b34bc8cb270a407b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288861,
  "host_pid": "9e6742732c60:1",
  "hash": "43058a8d171afdb3d2d7c30b9b05050011b0f05bd00889d3b7768a0d35d4a693",
  "cid": "QmV143058a8d171afdb3d2d7c30b9b05050011b0f05b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288861,
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
      "evaluated_at": 1760288861
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
  "sig": "ad7c8ea196b455ba9cc412b794bc824a8cd5f0f8150316edbbe9eea75c2ed00d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274747147
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '9bf7edfe04e96377'}}}