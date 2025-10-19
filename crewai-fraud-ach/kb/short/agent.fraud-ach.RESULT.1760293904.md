```json
{
  "id": "daa295346111b5dc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293904,
  "host_pid": "9e6742732c60:1",
  "hash": "ed4edc531fabdd51ab47698f9f8df164772d52bec7d64ade8bf142781094f285",
  "cid": "QmV1ed4edc531fabdd51ab47698f9f8df164772d52be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293904,
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
      "evaluated_at": 1760293905
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
  "sig": "0f074a51ec1cfcc1626d2d4fe16923cede499d120fe0176346e7e659268ec03a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031517905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 101585628, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'e8f76fb2eb784ea5'}}}