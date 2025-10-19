```json
{
  "id": "8cce2a5aee82c5e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289061,
  "host_pid": "9e6742732c60:1",
  "hash": "cdedc899e08697963688aaf606ed07cdab4ec576c3b255c5703430bc8168b63a",
  "cid": "QmV1cdedc899e08697963688aaf606ed07cdab4ec576",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289061,
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
      "evaluated_at": 1760289061
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
  "sig": "970051deff8b21ef76297578fee8398d4960a4ce9ad6ced09b2a4a7a1aa327a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271369125
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 17344208, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': 'b975113295de86ab'}}}