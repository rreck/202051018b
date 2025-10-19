```json
{
  "id": "e330a479735f4cd8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288819,
  "host_pid": "9e6742732c60:1",
  "hash": "a5f2cba68fffe34bb4b23d695b5a5a851dc5163ed30468f34b3e9d89110db2f5",
  "cid": "QmV1a5f2cba68fffe34bb4b23d695b5a5a851dc5163e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288819,
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
      "evaluated_at": 1760288819
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
  "sig": "47e2a7d10655148c04ca4ad7a3adfd5c5cee218f938f767348b8a1e96001685e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244807015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 10500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285764, 'matching_hash': 'e3fbbc71f2accf8f'}}}aly': {'fraud_detected': True, 'risk_score': 86, 'details': {'zscore': 4.68, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8942822}}}