```json
{
  "id": "dc5ce42181dc09fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291267,
  "host_pid": "9e6742732c60:1",
  "hash": "df4eebff6e1f82f481fb88bacc83e642c36aadff91cdc432566ad5058f32841c",
  "cid": "QmV1df4eebff6e1f82f481fb88bacc83e642c36aadff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291267,
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
      "evaluated_at": 1760291267
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
  "sig": "2267a6bebde3595e4b5509304daafe72c034a69c8e575629ddf3de065ddd4e32"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022300374
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 23808672, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': '0c9c3ceb4a82225f'}}}