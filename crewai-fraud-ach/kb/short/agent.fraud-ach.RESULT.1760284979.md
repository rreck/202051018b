```json
{
  "id": "139772b903660d01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760284979,
  "host_pid": "9e6742732c60:1",
  "hash": "05b9c4b7d091bf34a255ebd811214b4b7b8922f49c11e8b549b00e9df2cbae54",
  "cid": "QmV105b9c4b7d091bf34a255ebd811214b4b7b8922f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760284979,
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
      "evaluated_at": 1760284979
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
  "sig": "923699e3a16b8a6dd23f421384e201c217067e7efba205e65e06bcda5fbf575f"
}
```

Fraud detected: amount_anomaly (score: 77)
Transaction: 021000029388663
Details: {'amount_anomaly': {'fraud_detected': True, 'risk_score': 77, 'details': {'zscore': 3.75, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9795510}}}