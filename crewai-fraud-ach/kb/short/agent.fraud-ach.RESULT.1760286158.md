```json
{
  "id": "979b24124170dd7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286158,
  "host_pid": "9e6742732c60:1",
  "hash": "dee8d078180c2dcc075e41556119c83e7021d34b15570a24dc4c1a69868ff52e",
  "cid": "QmV1dee8d078180c2dcc075e41556119c83e7021d34b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286158,
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
      "evaluated_at": 1760286158
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
  "sig": "c9e40d6517fa0d6b0d2a1d560bb5eb5a807ceda6aeaf3dddd60f2f9b4084fea0"
}
```

Fraud detected: round_amount_pattern (score: 62)
Transaction: 031201462455734
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285763, 'matching_hash': '2de7efbdf08711e2'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}