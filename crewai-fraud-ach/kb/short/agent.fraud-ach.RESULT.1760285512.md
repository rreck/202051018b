```json
{
  "id": "2029903c8c9a863f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285512,
  "host_pid": "9e6742732c60:1",
  "hash": "4dcdc8ad36dfa68d77d1b1a79bd488cfe08807671d8675b8589c1b4c2689afec",
  "cid": "QmV14dcdc8ad36dfa68d77d1b1a79bd488cfe0880767",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285512,
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
      "evaluated_at": 1760285512
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "09f24d3e04b405babd2f94e985afecbb65e8788d3130f2ce08df859b2db6a56a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000027783214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 25714593, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760284979, 'matching_hash': '00d004b11e9e3015'}}}