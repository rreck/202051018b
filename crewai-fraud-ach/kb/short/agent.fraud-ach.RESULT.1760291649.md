```json
{
  "id": "2f23b2a718400df9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291649,
  "host_pid": "9e6742732c60:1",
  "hash": "d9328a45972c3295a0a7a503ab9f05d8cd67edd6fb632f839a045b1089d2d22e",
  "cid": "QmV1d9328a45972c3295a0a7a503ab9f05d8cd67edd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291649,
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
      "evaluated_at": 1760291649
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
  "sig": "62c794fb2f72aab2c10bf1b9186abc9e34d16fe37a327251ae62e06cd11a8d68"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596228885
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 79531380, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': '9b2dabf2ca05df4f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244096997', 'validation_error': 'Invalid routing number checksum'}}}