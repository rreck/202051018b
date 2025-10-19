```json
{
  "id": "c59e35a132a26f55",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289552,
  "host_pid": "9e6742732c60:1",
  "hash": "b3f902b70e0b6131048368cc78db3c4fbd2521aefea1909f9f7ae1d5a32f1f2f",
  "cid": "QmV1b3f902b70e0b6131048368cc78db3c4fbd2521ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289552,
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
      "evaluated_at": 1760289552
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
  "sig": "8a5d08182ae7aa814d7d2c6b333a462c82a722743e05fc11995818dc85c07161"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460708628
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285765, 'matching_hash': 'f97c6efa7b54b0cd'}}}