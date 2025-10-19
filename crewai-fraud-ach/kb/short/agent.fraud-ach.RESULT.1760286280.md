```json
{
  "id": "124c1f7809c1cde6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286280,
  "host_pid": "9e6742732c60:1",
  "hash": "182d0cb9929e552597726fb9261efb91bb762008bed8103f6a5c0399ae00ff03",
  "cid": "QmV1182d0cb9929e552597726fb9261efb91bb762008",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286280,
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
      "evaluated_at": 1760286280
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
  "sig": "52dc93cdc57ef02f212d745e9918451d4d0fc251e4a7cf48c39feef2654f9c68"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 026009597367941
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 186122120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285764, 'matching_hash': '5430161f1ba10767'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.53, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9306106}}}