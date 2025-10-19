```json
{
  "id": "aeb8ba80c7aa5ec2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289530,
  "host_pid": "9e6742732c60:1",
  "hash": "cc6c8f7a858396d494036a7e3cc3b5f1968623cb15c95d1db1cb2fe50c7d9f27",
  "cid": "QmV1cc6c8f7a858396d494036a7e3cc3b5f1968623cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289530,
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
      "evaluated_at": 1760289530
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
  "sig": "735b50032d9884e7315d0f0c8182989436a6b06642d9139327620b73f439d275"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598639172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': '9f277109cf79f7ea'}}}een': 1760285763, 'matching_hash': '565398b77a50d0ac'}}}