```json
{
  "id": "f2731699cc10d345",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285781,
  "host_pid": "9e6742732c60:1",
  "hash": "74a21d3f6f4cb049a4b3e39955c8f67c892daf5d4d052d4ce2d5cae881b97169",
  "cid": "QmV174a21d3f6f4cb049a4b3e39955c8f67c892daf5d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285781,
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
      "evaluated_at": 1760285781
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "569c771ff79ad2d570e6c52c1dff9672931e985271fc70e6d6f66aa5e4fc199a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009592568865
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760285763, 'matching_hash': 'ecded74c6845c7bc'}}}