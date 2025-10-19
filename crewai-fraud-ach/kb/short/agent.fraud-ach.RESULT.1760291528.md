```json
{
  "id": "3c0b6a8f40e9cdd1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291528,
  "host_pid": "9e6742732c60:1",
  "hash": "34c58e9f62567e6e07683f3367c546f635bc662dd7a9c809716c979c328361b3",
  "cid": "QmV134c58e9f62567e6e07683f3367c546f635bc662d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291528,
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
      "evaluated_at": 1760291528
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
  "sig": "2db7f21a9655fbbec1ff133a0b607cf21f33ff7a76e3618e0e9207175b177905"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247109361
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 16753581, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': '3efad933d2b7f9bd'}}}maly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.39, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8435125}}}