```json
{
  "id": "cedbb610cf167940",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291274,
  "host_pid": "9e6742732c60:1",
  "hash": "42fe6613949d284f19c9c28e46fbb951d6428bb32364846213bb189c7b60ecdf",
  "cid": "QmV142fe6613949d284f19c9c28e46fbb951d6428bb3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291274,
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
      "evaluated_at": 1760291274
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
  "sig": "3f8e0521358045e1baba39e989e6dea4223fce4b71ed5fc4d735d21cbab3364b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151593614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 70816572, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': '43945ca7b36522b2'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}