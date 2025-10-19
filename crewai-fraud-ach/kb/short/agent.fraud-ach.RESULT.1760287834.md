```json
{
  "id": "a922a12683eb85e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287834,
  "host_pid": "9e6742732c60:1",
  "hash": "091ace3e39e566469888b2dbf6830b614c011aa57730782f8613fedf30e96835",
  "cid": "QmV1091ace3e39e566469888b2dbf6830b614c011aa5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287834,
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
      "evaluated_at": 1760287834
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
  "sig": "e4f4ff3d0037e7f8676c2032bb0dcf1a803c39c3cf1e7f23e221cc376a6f66b0"
}
```

Fraud detected: round_amount_pattern (score: 74)
Transaction: 031201463734572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 37000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285763, 'matching_hash': '9877b0a7b07093eb'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}