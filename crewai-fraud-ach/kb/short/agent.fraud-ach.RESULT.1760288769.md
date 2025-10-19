```json
{
  "id": "df20b8e3f3cec879",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288769,
  "host_pid": "9e6742732c60:1",
  "hash": "9e9cbd9abb5f04ccddde08ee8d581d32e5b3a997a7a3fd216ab8041261d4301a",
  "cid": "QmV19e9cbd9abb5f04ccddde08ee8d581d32e5b3a997",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288769,
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
      "evaluated_at": 1760288769
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
  "sig": "1462d529982a872646d3527b437d9982d4ae72ed5d8b069000d03a85e3319a59"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028970082
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 29218525, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285765, 'matching_hash': 'a98af89fc7548453'}}}