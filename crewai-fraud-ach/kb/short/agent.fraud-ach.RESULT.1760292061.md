```json
{
  "id": "5fb513b87383d4b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292061,
  "host_pid": "9e6742732c60:1",
  "hash": "827dc9eeb9db0225edeb462b1823b5dfffa0811cfb34bf38e799104dbc9095c7",
  "cid": "QmV1827dc9eeb9db0225edeb462b1823b5dfffa0811c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292061,
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
      "evaluated_at": 1760292061
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
  "sig": "23ccecde1a862b611f698ce7cd842d14bb6bd3cf1db58c4828f390f2370c3839"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034981344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 71781444, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285765, 'matching_hash': '0030d58ae3a464b4'}}}