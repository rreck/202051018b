```json
{
  "id": "cbc737d6953815a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289393,
  "host_pid": "9e6742732c60:1",
  "hash": "f5107ea4a3d1c28ccfce7178d44cc84b679b81e8e489a40d177dee0e0a810140",
  "cid": "QmV1f5107ea4a3d1c28ccfce7178d44cc84b679b81e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289393,
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
      "evaluated_at": 1760289393
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
  "sig": "3ef64268ab9adb239f2dc58f39aa0e33460b9e2d19f43f6d407250fb23d33d2a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469691170
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 12200000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285763, 'matching_hash': '3e5e2db3f0853706'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '060557489', 'validation_error': 'Invalid routing number checksum'}}}