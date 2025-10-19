```json
{
  "id": "b299c6a3cb7edc83",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293916,
  "host_pid": "9e6742732c60:1",
  "hash": "b0c04be68c637fc4215ad5d1154eb318f4732f48f2ebd41d41e8086860b41571",
  "cid": "QmV1b0c04be68c637fc4215ad5d1154eb318f4732f48",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293916,
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
      "evaluated_at": 1760293916
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
  "sig": "a20ee7525c731a3a274f29cccf1a26abeca3a8e0d0d23afea85dcc33859a1fd8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469153369
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 20696016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285764, 'matching_hash': 'a6e88c6efc20349f'}}}maly': {'fraud_detected': True, 'risk_score': 90, 'details': {'zscore': 5.02, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9547605}}}