```json
{
  "id": "97212b6f0a023fc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294065,
  "host_pid": "9e6742732c60:1",
  "hash": "710151a1b2460a2feb88dd240e6f69f2e81db1570895ca1b80e0e5be7cff837c",
  "cid": "QmV1710151a1b2460a2feb88dd240e6f69f2e81db157",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294065,
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
      "evaluated_at": 1760294065
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
  "sig": "4d52042b8ef749f48984425568438fa88ef2ea710d051425a9d0369baca7ba77"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270759086
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 82859700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': 'eb79951538526d2c'}}}maly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.1, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6161479}}}