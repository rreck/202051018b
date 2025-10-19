```json
{
  "id": "a4f5c8c26871e818",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292207,
  "host_pid": "9e6742732c60:1",
  "hash": "71fa83f5d5ba1de3d96d5d43ca4eed398b254149a2f986bdb27e845292fa46f3",
  "cid": "QmV171fa83f5d5ba1de3d96d5d43ca4eed398b254149",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292207,
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
      "evaluated_at": 1760292207
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
  "sig": "e12aee0352487d057f1357683737b4b7d172dcc4ca7717a762d8f16ec0639c95"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000022377083
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 96000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285765, 'matching_hash': 'fc2d68d27512b7d3'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}