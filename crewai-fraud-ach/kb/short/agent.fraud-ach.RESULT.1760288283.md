```json
{
  "id": "ab20d6e03021ff3a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288283,
  "host_pid": "9e6742732c60:1",
  "hash": "6c1afaba4d2697c54678b87178444fb1756c404ef2e411f9afc1d4fe24bbf1b1",
  "cid": "QmV16c1afaba4d2697c54678b87178444fb1756c404e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288283,
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
      "evaluated_at": 1760288283
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
  "sig": "9ada95a2cd16aa3ea3c4e650c294a179c68906643e26429f2e32729ad6f97502"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462408143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 42788504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285765, 'matching_hash': '36407d3e627869a5'}}}