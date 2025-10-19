```json
{
  "id": "8b60236d63db6551",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286163,
  "host_pid": "9e6742732c60:1",
  "hash": "d6f4bca87acb535f62d3b75ccaf3da6e12c018fc6ac9ce83aa63c2ab201cbcec",
  "cid": "QmV1d6f4bca87acb535f62d3b75ccaf3da6e12c018fc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286163,
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
      "evaluated_at": 1760286163
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
  "sig": "bcf12368d7c9f57205f50c7ec859a48b6a216d930ee9e11ea94a2f35d05c0e28"
}
```

Fraud detected: round_amount_pattern (score: 62)
Transaction: 031201465841026
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285765, 'matching_hash': 'e2a83dab91a99cc0'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}