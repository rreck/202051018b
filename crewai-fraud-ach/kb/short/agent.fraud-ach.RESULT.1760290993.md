```json
{
  "id": "941f7a767e9bbd5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290993,
  "host_pid": "9e6742732c60:1",
  "hash": "1c5157a374d244ba9ae60d554468a4c6c5fc46fd0c39ec620bfdecf4d058a5a7",
  "cid": "QmV11c5157a374d244ba9ae60d554468a4c6c5fc46fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290993,
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
      "evaluated_at": 1760290993
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
  "sig": "5dda61d80d616c3ea29d48dfb9d142e42c0ff0a861f02702cd0c5a2133e2b03c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243277611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 23090216, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': '2d64263c5765c58b'}}}