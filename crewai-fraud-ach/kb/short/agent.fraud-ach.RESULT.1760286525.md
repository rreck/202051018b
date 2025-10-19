```json
{
  "id": "2274f8cb07b5a800",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286525,
  "host_pid": "9e6742732c60:1",
  "hash": "4d971702efc9315a1bd6b0d533f80db6c37859d2374956de544988162eb2e2ec",
  "cid": "QmV14d971702efc9315a1bd6b0d533f80db6c37859d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286525,
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
      "evaluated_at": 1760286525
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
  "sig": "a5e04f2ef788e8dc970560a3856f0a34c959d2b94ade220cd07dd688ed4a5623"
}
```

Fraud detected: amount_anomaly (score: 75)
Transaction: 026009592955504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 239379952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285765, 'matching_hash': 'e4b1ef1aea3a67a1'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.2, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8549284}}}