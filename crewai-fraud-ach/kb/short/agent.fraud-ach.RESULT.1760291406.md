```json
{
  "id": "8a380aa4e0b5e4ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291406,
  "host_pid": "9e6742732c60:1",
  "hash": "f880a70f380f30b36cf596e312045133e093a756421180d2ff2033acb09c56f6",
  "cid": "QmV1f880a70f380f30b36cf596e312045133e093a756",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291406,
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
      "evaluated_at": 1760291406
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
  "sig": "3cdba88708a8b641e19ede303d05e73942c71332b3a0af647966de995969b9ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243367348
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 56516592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285765, 'matching_hash': 'a37b6eb1b4e3b31b'}}}