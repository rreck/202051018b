```json
{
  "id": "87c4492a2b3370f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286792,
  "host_pid": "9e6742732c60:1",
  "hash": "3e89ed8c47ee6dd8dc2b8eff121b053a8680535425afae88f1a5ec47f2a4d2be",
  "cid": "QmV13e89ed8c47ee6dd8dc2b8eff121b053a86805354",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286792,
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
      "evaluated_at": 1760286792
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
  "sig": "3a1ef391ef9083961f9031d9d001be35d0da918b43c2f499cf33f1c710383652"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 063100275758456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 348434513, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285765, 'matching_hash': 'e3feb2a34db32d71'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.58, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9417149}}}