```json
{
  "id": "e3f73ed503ec0d2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287213,
  "host_pid": "9e6742732c60:1",
  "hash": "901c45946d955f7cf3ca6cf9c38767a7fc9508731b06c6fe0a29051a764d7c40",
  "cid": "QmV1901c45946d955f7cf3ca6cf9c38767a7fc950873",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287213,
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
      "evaluated_at": 1760287213
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
  "sig": "8ee54cef35760dc8254ca48cfc6b0a7ee7d52e4162755dfff7d32165b3ed9111"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272135261
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 40876032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760284979, 'matching_hash': 'c71937e0bf846771'}}}'fraud_detected': True, 'risk_score': 78, 'details': {'zscore': 3.83, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9966572}}}