```json
{
  "id": "e8d4301fad1eead0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291179,
  "host_pid": "9e6742732c60:1",
  "hash": "468db03c31874fc21e609f4115b047210764de81571ff8c6503946aee2a8aa1b",
  "cid": "QmV1468db03c31874fc21e609f4115b047210764de81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291179,
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
      "evaluated_at": 1760291179
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
  "sig": "89ed89ef2383d733fc81c77e34010b6373f48bd3a31ca049d8c29c1e19cd263d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022225777
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 13724997, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': '9e191c483430cef0'}}}maly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.93, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7623976}}}