```json
{
  "id": "5cb854d340043c2d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287236,
  "host_pid": "9e6742732c60:1",
  "hash": "6de6fbf134c19513cff7c76100b0f4b78d2a7560ea683077fdb99324e9b24e7c",
  "cid": "QmV16de6fbf134c19513cff7c76100b0f4b78d2a7560",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287236,
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
      "evaluated_at": 1760287236
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
  "sig": "54eb8df210a518e3c3196ec01ea967fc8af55a80600890db1a8380aa729889b2"
}
```

Fraud detected: duplicate_transaction (score: 70)
Transaction: 063100274851410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 56, 'details': {'transaction_count': 53, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285763, 'matching_hash': '05e1730ec720465d'}}}een': 1760285763, 'matching_hash': '1df4316d53c749d8'}}}