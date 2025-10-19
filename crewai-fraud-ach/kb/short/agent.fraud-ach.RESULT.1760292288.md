```json
{
  "id": "7a5f297d645be918",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292288,
  "host_pid": "9e6742732c60:1",
  "hash": "c20bd18141afd77f262b0725c9ed4b910cd424f67826b4939b747e358c7d5680",
  "cid": "QmV1c20bd18141afd77f262b0725c9ed4b910cd424f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292288,
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
      "evaluated_at": 1760292288
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
  "sig": "df37c5364788668c5034a1dd0d340ba56c09bd2be75d84f9234de732ad2bb35e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271240415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 22828756, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285765, 'matching_hash': '8c20097da64de4ba'}}}