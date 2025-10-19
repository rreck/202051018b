```json
{
  "id": "95a0c55ca5afbd5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289515,
  "host_pid": "9e6742732c60:1",
  "hash": "bbae5b0664c860093783654792cc08e215fa8cadc10ae0cc53059e367586ace8",
  "cid": "QmV1bbae5b0664c860093783654792cc08e215fa8cad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289515,
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
      "evaluated_at": 1760289515
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
  "sig": "58060f49630f69ec864fc6343e4d76590f47d4c9d361e343ab6f6a4027acc8db"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037820415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285765, 'matching_hash': 'e2c6bf9b42825543'}}}