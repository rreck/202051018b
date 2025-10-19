```json
{
  "id": "a3ee1fd9eb916b9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292115,
  "host_pid": "9e6742732c60:1",
  "hash": "d7ab0b90965e8f475d363cdcaa2a2087cf8dc34eaf5b724930bcc3b5d079acfb",
  "cid": "QmV1d7ab0b90965e8f475d363cdcaa2a2087cf8dc34e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292115,
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
      "evaluated_at": 1760292115
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
  "sig": "b587afabc3aa78f0ca3e108c48a2d49298a775e9bd45c86a82654f84f495e3fd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021865843
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 47500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285765, 'matching_hash': '0e7cb19dffe9e37d'}}}