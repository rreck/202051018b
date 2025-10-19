```json
{
  "id": "c1814819fabead1a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293970,
  "host_pid": "9e6742732c60:1",
  "hash": "bbf882285922c44619965a6e2f82a73689962e7b92932c4ad3cf30e6dd61ed9e",
  "cid": "QmV1bbf882285922c44619965a6e2f82a73689962e7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293970,
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
      "evaluated_at": 1760293970
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "fd7b974b216addba882f57b9b76b71ea6c1ddb90e561c10b65d32ba7698a6df1"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 021000020489818
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 1931643625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': 'b3efe19f99a87213'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.39, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8435125}}}