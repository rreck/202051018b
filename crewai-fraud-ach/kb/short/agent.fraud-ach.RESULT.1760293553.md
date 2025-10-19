```json
{
  "id": "935ac310e67c5acd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293553,
  "host_pid": "9e6742732c60:1",
  "hash": "f4c9e957a9359460f13375dfaad01d6b3df8804503e0ce0f7bfcce6e0d7ffed5",
  "cid": "QmV1f4c9e957a9359460f13375dfaad01d6b3df88045",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293553,
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
      "evaluated_at": 1760293553
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
  "sig": "6b2be21176849eb442b8a9e5d5c198563403cc64c62285c4d68906bf092f0753"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275563549
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 93921685, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'a33681b350a57503'}}}maly': {'fraud_detected': True, 'risk_score': 81, 'details': {'zscore': 4.15, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8018549}}}