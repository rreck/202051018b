```json
{
  "id": "67413ef59ece45b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290654,
  "host_pid": "9e6742732c60:1",
  "hash": "e300f124fd654381caac2eda4bb3ce1b2f22bd9e1850fd0e68a91be01d5d4284",
  "cid": "QmV1e300f124fd654381caac2eda4bb3ce1b2f22bd9e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290654,
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
      "evaluated_at": 1760290654
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
  "sig": "f8b36db757e8047d1dd297825469bb9e6579d903558a7d46822e789d9c3cd3c6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022691878
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': 'a2c26d052e86193d'}}}