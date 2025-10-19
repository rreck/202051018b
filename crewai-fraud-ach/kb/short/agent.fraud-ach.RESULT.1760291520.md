```json
{
  "id": "70cccc554de3c7ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291520,
  "host_pid": "9e6742732c60:1",
  "hash": "651eee6b9d46ce5ff55666fdfa99a33164af38a3f256bb37e29a0e4c230860a7",
  "cid": "QmV1651eee6b9d46ce5ff55666fdfa99a33164af38a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291520,
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
      "evaluated_at": 1760291520
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
  "sig": "f987a408e0bb11cb6ead5787dc8a59a2e535c89b8d373cfbc9036b925dea8f8a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028779608
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 53272752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': 'f4a7019387fd02e9'}}}