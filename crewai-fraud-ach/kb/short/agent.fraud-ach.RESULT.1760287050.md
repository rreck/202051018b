```json
{
  "id": "1ccbbb1a028c77bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287050,
  "host_pid": "9e6742732c60:1",
  "hash": "2bb98d1760042fc19629ff1f0ffc671b941c00718f3b41b2c01feb2fdf353942",
  "cid": "QmV12bb98d1760042fc19629ff1f0ffc671b941c0071",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287050,
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
      "evaluated_at": 1760287050
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
  "sig": "0b89821e2abc61ae000a29cf8df5ddb576767cb4206f42cab37abc94d4e47340"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201467961793
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285765, 'matching_hash': '7ef856857e97207f'}}}