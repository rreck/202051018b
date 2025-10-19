```json
{
  "id": "a8769edd606c7aa6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289361,
  "host_pid": "9e6742732c60:1",
  "hash": "ca9a2b2c99bf8b757eaa795a3e5fd03c451be989b01bfd2338f4918088488ab2",
  "cid": "QmV1ca9a2b2c99bf8b757eaa795a3e5fd03c451be989",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289361,
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
      "evaluated_at": 1760289361
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
  "sig": "6378e54841ed3846a6d23f2ad7a788ecfef963ea0ec19ee762596faefe65996c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150046055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 47562559, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285764, 'matching_hash': 'b44312efb353b904'}}}maly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.48, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8595712}}}