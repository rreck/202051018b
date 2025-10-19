```json
{
  "id": "8eb4da7f2d18d6e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288964,
  "host_pid": "9e6742732c60:1",
  "hash": "954fb23b2e752349b7fe5379d08c60fef73db20a4a2fe64d089f5b85882c488a",
  "cid": "QmV1954fb23b2e752349b7fe5379d08c60fef73db20a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288964,
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
      "evaluated_at": 1760288964
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
  "sig": "3c32339e5ec50361d840b131f8db0eeb1306998c0cf5c9ebaa16125484437a20"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025325708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 35125577, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285765, 'matching_hash': '23dd43a9dda0a05d'}}}