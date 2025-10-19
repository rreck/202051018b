```json
{
  "id": "44743ab06be5b2a5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292153,
  "host_pid": "9e6742732c60:1",
  "hash": "563e5b6c296fc497bbe53401d153075f40a052b6f8875e568efde9c240489e41",
  "cid": "QmV1563e5b6c296fc497bbe53401d153075f40a052b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292153,
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
      "evaluated_at": 1760292153
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
  "sig": "537d79a16b893d7c2d676e512128082550e69dbb77e76405c9254365630f2ab7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244410720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 13466455, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': 'eab520de73a5b8cf'}}}