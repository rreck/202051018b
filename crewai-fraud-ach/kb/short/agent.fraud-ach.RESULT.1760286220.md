```json
{
  "id": "b52b6817bcc033c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286220,
  "host_pid": "9e6742732c60:1",
  "hash": "502a8f825b0fa7aecad221da047839902f0c7e5110bd1472c0725f9786ae2e01",
  "cid": "QmV1502a8f825b0fa7aecad221da047839902f0c7e51",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286220,
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
      "evaluated_at": 1760286220
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
  "sig": "02db42da863f0440e91ae20de825f39b58b67d0180dd6790eabccb7d4083fe0e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100270344488
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285764, 'matching_hash': 'ec3de169da630728'}}}