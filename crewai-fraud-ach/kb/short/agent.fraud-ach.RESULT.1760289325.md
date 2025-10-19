```json
{
  "id": "f2ac931292f3ae4c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289325,
  "host_pid": "9e6742732c60:1",
  "hash": "9ee293ffc4abaa60f62f20359df0d4cc5bab5c2d8ead7586605903819aa8d88c",
  "cid": "QmV19ee293ffc4abaa60f62f20359df0d4cc5bab5c2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289325,
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
      "evaluated_at": 1760289325
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
  "sig": "cf47f7ebba1b94faadedb20277530b51fc566ca518281e0ab7ca21230bfad7e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241012804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 33138000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285763, 'matching_hash': 'ba9ba43773b08e05'}}}