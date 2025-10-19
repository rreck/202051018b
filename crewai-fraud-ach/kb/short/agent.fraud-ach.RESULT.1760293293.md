```json
{
  "id": "7747526aca1428d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293293,
  "host_pid": "9e6742732c60:1",
  "hash": "82b41ae5269e284ce7c12f66aa7f89ab8b80c1bbd3fa3284d7bec4a4336ec9b7",
  "cid": "QmV182b41ae5269e284ce7c12f66aa7f89ab8b80c1bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293293,
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
      "evaluated_at": 1760293293
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "3a6b54fcafe74cc66bef68a3e2407c4c79d0868bb6c631d44e9460770ffeafb2"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000022377083
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 107500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285765, 'matching_hash': 'fc2d68d27512b7d3'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}