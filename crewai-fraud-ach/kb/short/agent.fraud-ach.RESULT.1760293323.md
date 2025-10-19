```json
{
  "id": "8094382046488119",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293323,
  "host_pid": "9e6742732c60:1",
  "hash": "9bdd4b4adaaa113f99a6eee8f6954f92e52e62468f5a40ee2546cc962c2b650a",
  "cid": "QmV19bdd4b4adaaa113f99a6eee8f6954f92e52e6246",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293323,
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
      "evaluated_at": 1760293323
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
  "sig": "4b8bf4783c8035088e0cdfe15af7c96acca31c679d56cb3adc0d1357c38a1555"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465124688
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 35543448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': 'c4099eb9aeb13a11'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '650095545', 'validation_error': 'Invalid routing number checksum'}}}