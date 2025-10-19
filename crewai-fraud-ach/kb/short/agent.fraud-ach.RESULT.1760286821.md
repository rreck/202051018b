```json
{
  "id": "3c59693d58f63786",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286821,
  "host_pid": "9e6742732c60:1",
  "hash": "35e1edea14187f558c4a1b54494b8b50191757a1207ff6d7978f1e8de3aa2612",
  "cid": "QmV135e1edea14187f558c4a1b54494b8b50191757a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286821,
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
      "evaluated_at": 1760286821
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
  "sig": "36f5d00f02945b12e5e6be9387cc4ed75f98e2a1ad90ba2f81722ed963c1d685"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000037652029
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10842692, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285765, 'matching_hash': '6ae01c61248929d6'}}}