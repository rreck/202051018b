```json
{
  "id": "530555ed96faf4de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293815,
  "host_pid": "9e6742732c60:1",
  "hash": "ee9fc91c573b8c6147ca2408406db007b45c2f6c377f9e6bd829440d2e077a7e",
  "cid": "QmV1ee9fc91c573b8c6147ca2408406db007b45c2f6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293815,
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
      "evaluated_at": 1760293815
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
  "sig": "a82f7363c3ba2c00638b33530aa6c499355e7f0cda95a20db2eaa98715aeba21"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271528987
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 91985390, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '52a7e62e45a672d0'}}}