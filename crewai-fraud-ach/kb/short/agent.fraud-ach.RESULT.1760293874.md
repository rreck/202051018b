```json
{
  "id": "a887613c7bc8e6d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293874,
  "host_pid": "9e6742732c60:1",
  "hash": "8ba012b8b21349011a6970bf817c01f2852ec31c8626d9231e4c81d83773889c",
  "cid": "QmV18ba012b8b21349011a6970bf817c01f2852ec31c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293874,
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
      "evaluated_at": 1760293874
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
  "sig": "ffcef4a48886f638ad59f62477e860d7434326c95ae80cf3c7e73001b691ea7a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244291071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 28733887, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '1f8fb3dc368ee7c3'}}}maly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 4.0, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7743228}}}