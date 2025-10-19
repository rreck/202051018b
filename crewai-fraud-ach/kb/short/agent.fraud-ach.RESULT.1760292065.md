```json
{
  "id": "f17f9a2a2c5ca838",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292065,
  "host_pid": "9e6742732c60:1",
  "hash": "7d84bc8edfb4f818f74f7153457e5da1d17558e4cd36b677755eb6750b894433",
  "cid": "QmV17d84bc8edfb4f818f74f7153457e5da1d17558e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292065,
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
      "evaluated_at": 1760292065
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
  "sig": "29b7e0abfddecaddb30d823c8dae53faa1ee9a6f56e42be93d02b762c96450a0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593456245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 91055097, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285764, 'matching_hash': '5bbbd28055422217'}}}