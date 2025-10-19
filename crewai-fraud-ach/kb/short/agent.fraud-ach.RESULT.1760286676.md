```json
{
  "id": "6d6467aa3b40b3cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286676,
  "host_pid": "9e6742732c60:1",
  "hash": "2fd4eb42f9311317150b780faf343b569cc053f88366e86c8edd17442dacb753",
  "cid": "QmV12fd4eb42f9311317150b780faf343b569cc053f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286676,
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
      "evaluated_at": 1760286676
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
  "sig": "934686606ba94fc8895bbf72f16c0f46f78a094bbdc4939f0761e5f4a2eaeea9"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 026009591978167
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 33000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 32, 'first_seen': 1760285765, 'matching_hash': '6b05f8817543e1fe'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}