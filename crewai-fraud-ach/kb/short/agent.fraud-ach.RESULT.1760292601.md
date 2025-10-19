```json
{
  "id": "4d58228742cf4320",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292601,
  "host_pid": "9e6742732c60:1",
  "hash": "8283a8132aa58fd2320b34bc5f42b228b8a1c50009c64749787b06c5d4552457",
  "cid": "QmV18283a8132aa58fd2320b34bc5f42b228b8a1c500",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292601,
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
      "evaluated_at": 1760292601
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
  "sig": "4915dd5cb0b8f0949ce7df53b5ed141cfc3b220144fee7386cea6bdb09115e60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591169500
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 39957393, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '9cbc2ba8ece9eaee'}}}