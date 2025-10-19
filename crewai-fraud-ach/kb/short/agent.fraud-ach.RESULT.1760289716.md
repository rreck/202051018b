```json
{
  "id": "f101413ac3d9859d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289716,
  "host_pid": "9e6742732c60:1",
  "hash": "878ef9c6a446929a562e1ce448f1e0f37f459e2d612abb038ebe268d0f1b3aae",
  "cid": "QmV1878ef9c6a446929a562e1ce448f1e0f37f459e2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289716,
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
      "evaluated_at": 1760289716
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
  "sig": "6b789a556fc5722303ef54d127c08cc8557a2bbace324e008944acda2679c768"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028017264
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 59566093, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285763, 'matching_hash': '707a4137bac9b143'}}}