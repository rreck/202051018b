```json
{
  "id": "f417b92e3a8443ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293822,
  "host_pid": "9e6742732c60:1",
  "hash": "9d25278e9501d701c87013cbbb0a71de3ed31f9410ce99f2a2fd67fd14635300",
  "cid": "QmV19d25278e9501d701c87013cbbb0a71de3ed31f94",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293822,
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
      "evaluated_at": 1760293822
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
  "sig": "90559ec5023120472d4318010bc747b6d9e1da545e1f90805a08e0f7c0b143fd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597475256
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 53606748, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': 'c99ab431a9f6998c'}}}}