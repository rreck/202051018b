```json
{
  "id": "ac0dd365f4f12421",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286764,
  "host_pid": "9e6742732c60:1",
  "hash": "b64611f4b966e99c676e16cc220c64f0d7ba80d39d245a9b65808105c8e7a61c",
  "cid": "QmV1b64611f4b966e99c676e16cc220c64f0d7ba80d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286764,
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
      "evaluated_at": 1760286764
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
  "sig": "9a8af4f99cafb43fb7b0ccf84221c3186a8458bc7c922036ddee56bd99ca631b"
}
```

Fraud detected: amount_anomaly (score: 71)
Transaction: 121000240089409
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 221005080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285765, 'matching_hash': 'a79d0bf31de09717'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6139030}}}