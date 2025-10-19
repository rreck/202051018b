```json
{
  "id": "090d682c5166d408",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289476,
  "host_pid": "9e6742732c60:1",
  "hash": "2e421dd5ac9d5d07921b8d9ea3d57334c39f4597aa8c76e83e2139345d880824",
  "cid": "QmV12e421dd5ac9d5d07921b8d9ea3d57334c39f4597",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289476,
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
      "evaluated_at": 1760289476
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
  "sig": "b3bf6b9807f0ef5e8fa5fd4157bc082e6d938cbc3ba0ef914588090f88fe645c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277311413
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285763, 'matching_hash': '8eaabbab3b444a6b'}}}