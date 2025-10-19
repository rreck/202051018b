```json
{
  "id": "cd664d87e08b3649",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291182,
  "host_pid": "9e6742732c60:1",
  "hash": "0c0def4a066f118aa0e3ab65488c4f4e49a6163b8561c890914eca34f2945935",
  "cid": "QmV10c0def4a066f118aa0e3ab65488c4f4e49a6163b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291182,
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
      "evaluated_at": 1760291182
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
  "sig": "8b848fa454c7e55afc59507b3440b2a5cbebc17710d2470e01858fd0d2b4802d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150315138
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 58269510, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': '420167e0317803c0'}}}