```json
{
  "id": "e979f7914193b1d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287779,
  "host_pid": "9e6742732c60:1",
  "hash": "b293d6132c6d1db33ffdadc178100ec65c305ba10f0cadf8daf8d862fae019c1",
  "cid": "QmV1b293d6132c6d1db33ffdadc178100ec65c305ba1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287779,
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
      "evaluated_at": 1760287779
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
  "sig": "940d43c7e39c9ee8c8234d6365c64212eaac0b383126860a1fd645a51a32f3fb"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 121000244206130
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285764, 'matching_hash': '13fbcd8431ec0e21'}}}764, 'matching_hash': '09f46afbb4d14766'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.22, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8595712}}}