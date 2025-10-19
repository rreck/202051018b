```json
{
  "id": "c9697342aa0e006c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289944,
  "host_pid": "9e6742732c60:1",
  "hash": "1eb306ffa00b14a73bae48be81f9bcfbebd7fb38dc552c8ea827ed441f86f689",
  "cid": "QmV11eb306ffa00b14a73bae48be81f9bcfbebd7fb38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289944,
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
      "evaluated_at": 1760289944
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
  "sig": "506fba83a20be6dcc22bfe1a2a55061088e696f2dc1daa93c8959e593277f591"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469927048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 40815451, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': '982ed2d64f96a5b2'}}}