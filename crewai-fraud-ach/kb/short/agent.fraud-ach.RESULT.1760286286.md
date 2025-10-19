```json
{
  "id": "d0cdbc2103cee2a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286286,
  "host_pid": "9e6742732c60:1",
  "hash": "ea0e72324b5615ec1b2401df6183bf145fe6cb6c338ad117164eba308f021d06",
  "cid": "QmV1ea0e72324b5615ec1b2401df6183bf145fe6cb6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286286,
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
      "evaluated_at": 1760286286
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
  "sig": "2cf2e3f7a8c85a639ea1e81de2ed23cfde3ddc004b77e4ac3079ca5022df1074"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201466004729
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285765, 'matching_hash': '1e26fed2c08b1370'}}}