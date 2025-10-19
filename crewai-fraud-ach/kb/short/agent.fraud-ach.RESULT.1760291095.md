```json
{
  "id": "d98ad31d4b951862",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291095,
  "host_pid": "9e6742732c60:1",
  "hash": "fd6fb74d096e8bbbb2ad3608c950f55a86a2606a21e5305d514faabad2ede301",
  "cid": "QmV1fd6fb74d096e8bbbb2ad3608c950f55a86a2606a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291095,
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
      "evaluated_at": 1760291095
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
  "sig": "71fc79e50d28583c6d10efaed9bcbd1f6e04d538f7c39ce77517297a1195316a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025159939
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 78795944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': 'bd88da65ef85df29'}}}maly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.93, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7623976}}}