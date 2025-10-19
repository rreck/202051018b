```json
{
  "id": "1d2ab1e8727cbaed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291403,
  "host_pid": "9e6742732c60:1",
  "hash": "8ee6c1b2be3c5a92c2e535e09960276ddb88bcec38afbfe519bb31de9e997719",
  "cid": "QmV18ee6c1b2be3c5a92c2e535e09960276ddb88bcec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291403,
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
      "evaluated_at": 1760291403
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
  "sig": "09c4736f31d122414a28dca127b22d6d6c95e046b6759e7f1a956aaf477a7102"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029384681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 16034100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285764, 'matching_hash': '45a3ccbce684d395'}}}