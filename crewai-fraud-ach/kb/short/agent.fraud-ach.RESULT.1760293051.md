```json
{
  "id": "1c9a000e00eac722",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293051,
  "host_pid": "9e6742732c60:1",
  "hash": "087b597010bb0f7fb2376eabd24030f7033c0a6a94f2763b4e6ea02d2c8296f6",
  "cid": "QmV1087b597010bb0f7fb2376eabd24030f7033c0a6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293051,
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
      "evaluated_at": 1760293051
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
  "sig": "da4749c8d55ec0cc5b55b59fd65553eb98b84d0b500550dbf124a6fab129dd87"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000022377083
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 105000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285765, 'matching_hash': 'fc2d68d27512b7d3'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}