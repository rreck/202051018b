```json
{
  "id": "6b701dc9c6f7bdc3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289218,
  "host_pid": "9e6742732c60:1",
  "hash": "2a38576ae00416759b6c0a35b4a5ba6dff74e1b7321ded14a42cc87166ff5ed4",
  "cid": "QmV12a38576ae00416759b6c0a35b4a5ba6dff74e1b7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289218,
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
      "evaluated_at": 1760289218
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
  "sig": "3510a4f872ce32a3d82eb9cdec73ecb40ddb24b5afdb9806104aea645764a56b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591362528
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 50014575, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285763, 'matching_hash': '85f76e3ae9d0eff6'}}}