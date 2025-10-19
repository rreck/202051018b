```json
{
  "id": "a07cff5a8a686319",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290037,
  "host_pid": "9e6742732c60:1",
  "hash": "8c8a148b233652402b817252e727bdc5f900f8b42d35419a42e50a6ee2afc0ab",
  "cid": "QmV18c8a148b233652402b817252e727bdc5f900f8b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290037,
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
      "evaluated_at": 1760290037
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
  "sig": "1a25ef7b1eb52fa7316cd06c41292e66e7eb7ef4609bcae9363e17338759612c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595927429
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 20243020, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': 'ad7b7e4988d8fb8c'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}