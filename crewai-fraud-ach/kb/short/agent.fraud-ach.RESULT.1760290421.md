```json
{
  "id": "4224fcb747728271",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290421,
  "host_pid": "9e6742732c60:1",
  "hash": "f91aef045248227b65461cb189679aff9dd81b8a019b152b223a73b99b29e3e9",
  "cid": "QmV1f91aef045248227b65461cb189679aff9dd81b8a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290421,
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
      "evaluated_at": 1760290421
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
  "sig": "8d3f9e2b7aa9180b5c7d1b7060d4194457763d25c025419a11d96c5d670eda37"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591167362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 46810800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': '24df3db171a5add1'}}}aly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.1, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6161479}}}