```json
{
  "id": "2e22f5589a5a86c5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285279,
  "host_pid": "9e6742732c60:1",
  "hash": "a83f53b148ebb7d338a8160f752abee05504d34ffc0569ae8e4c67cd2845405c",
  "cid": "QmV1a83f53b148ebb7d338a8160f752abee05504d34f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285279,
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
      "evaluated_at": 1760285279
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "21fa0d95b20419f87e0335f2ea18b571ba3d863aab4a81b5da51d8eb002d8ecb"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12641820, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}