```json
{
  "id": "b2a773bec033a1c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286135,
  "host_pid": "9e6742732c60:1",
  "hash": "a96f418e31a551b6b45fe69a8da9fad7705facd02a095953f7af0438de53050f",
  "cid": "QmV1a96f418e31a551b6b45fe69a8da9fad7705facd0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286135,
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
      "evaluated_at": 1760286135
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
  "sig": "fe58bd5d0a0a134ba537a925fb596377ac715b52daaf69dd55ed360600823988"
}
```

Fraud detected: round_amount_pattern (score: 62)
Transaction: 111000022377083
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285765, 'matching_hash': 'fc2d68d27512b7d3'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}