```json
{
  "id": "168c1db826b292c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289150,
  "host_pid": "9e6742732c60:1",
  "hash": "352a5ace4888c8c9660613ccbd15def291b41ff82112cc06720aa8b61b260beb",
  "cid": "QmV1352a5ace4888c8c9660613ccbd15def291b41ff8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289150,
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
      "evaluated_at": 1760289150
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
  "sig": "cca0f75e5ca5231a8061e33669903249ab50c4b3a4213848a9de8fa6ba942480"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243028505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 11858110, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285763, 'matching_hash': '47e30fe250bb416c'}}}