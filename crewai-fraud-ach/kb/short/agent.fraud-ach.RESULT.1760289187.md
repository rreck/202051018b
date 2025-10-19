```json
{
  "id": "eee1c170056a408e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289187,
  "host_pid": "9e6742732c60:1",
  "hash": "fdeca27659977b86cc0d94375ea653c8228bfd634926649b265928d242656dcd",
  "cid": "QmV1fdeca27659977b86cc0d94375ea653c8228bfd63",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289187,
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
      "evaluated_at": 1760289187
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
  "sig": "9c82293b68825164d400ca014d56dde73cae0b856fb8fd758dfc66c52a7af78f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034782199
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 12615348, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': '89ad1f50f76a063c'}}}