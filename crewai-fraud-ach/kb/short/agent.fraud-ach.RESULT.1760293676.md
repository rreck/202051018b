```json
{
  "id": "5f555b6cce67668c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293676,
  "host_pid": "9e6742732c60:1",
  "hash": "95f0daec159f839125df638f541cede667e91e8f13b7b4567dfb066704eed66c",
  "cid": "QmV195f0daec159f839125df638f541cede667e91e8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293676,
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
      "evaluated_at": 1760293676
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
  "sig": "1be98853a1a48bb694a5f147176a0437a03f4e54b67b0556f8e9014f382f1b27"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241784115
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 100339073, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': 'd8ced4219e23835b'}}}