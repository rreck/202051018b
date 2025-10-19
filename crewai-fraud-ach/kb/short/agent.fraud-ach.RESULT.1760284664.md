```json
{
  "id": "6b31eee9a4137d45",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760284664,
  "host_pid": "rreck-MS-7D25:2442532",
  "hash": "05b9c4b7d091bf34a255ebd811214b4b7b8922f49c11e8b549b00e9df2cbae54",
  "cid": "QmV105b9c4b7d091bf34a255ebd811214b4b7b8922f4",
  "aicp": {
    "prov": {
      "issuer": "rreck-MS-7D25:2442532",
      "created_at": 1760284664,
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
      "evaluated_at": 1760284664
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
  "sig": "8948e7dbe067d4849c4d33cbc318c2d18aa795e7e38af4541f029e93560e97a7"
}
```

Fraud detected: amount_anomaly (score: 77)
Transaction: 021000029388663
Details: {'amount_anomaly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.75, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9795510}}}