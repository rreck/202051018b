```json
{
  "id": "d186ba3682305c44",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289473,
  "host_pid": "9e6742732c60:1",
  "hash": "3f80198d694e4a85046bb3b049073dc6b21b72d4412f51e9311971dc855cc2dc",
  "cid": "QmV13f80198d694e4a85046bb3b049073dc6b21b72d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289473,
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
      "evaluated_at": 1760289473
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
  "sig": "4c8582c4c833315e53cbe08ee026f703373a211884b22d0b813c132abde46e32"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157447901
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 16767156, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285765, 'matching_hash': '08b33f5611b85fcf'}}}