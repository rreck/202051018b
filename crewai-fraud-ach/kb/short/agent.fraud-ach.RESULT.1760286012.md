```json
{
  "id": "481dd2549edeff9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286012,
  "host_pid": "9e6742732c60:1",
  "hash": "f1df1abaee5c27ba11489e8d73a1da9b4db650a2369d79d1fd60b30636bcd846",
  "cid": "QmV1f1df1abaee5c27ba11489e8d73a1da9b4db650a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286012,
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
      "evaluated_at": 1760286012
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "f431f4f1c8d55772e428d663b074df7f65ee88112acb49d84f5d745e5ce94c84"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 044000032002639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 87437075, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285765, 'matching_hash': '27a8182d1a86d123'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 7948825}}}