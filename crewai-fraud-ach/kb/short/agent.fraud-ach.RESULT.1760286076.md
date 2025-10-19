```json
{
  "id": "b7beb9ba3f2415a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286076,
  "host_pid": "9e6742732c60:1",
  "hash": "3f4e237595d726c936b6a382733dd84a3aa270524691d285f185157c1d01ca71",
  "cid": "QmV13f4e237595d726c936b6a382733dd84a3aa27052",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286076,
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
      "evaluated_at": 1760286076
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
  "sig": "9dc3de3ddc11b8be0ef9661d4eed20f0d469d8d13182eb07ad4e26b3f1a7e81f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201462765128
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285765, 'matching_hash': 'e332841741f2145e'}}}