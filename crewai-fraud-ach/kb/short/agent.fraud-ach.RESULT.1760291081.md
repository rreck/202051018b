```json
{
  "id": "b2ccc2b7c3b9ee39",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291081,
  "host_pid": "9e6742732c60:1",
  "hash": "8c74d75ebba05dbb7ef3af351084ce18784cffa4023cc0af4fcd6a32f852e8f3",
  "cid": "QmV18c74d75ebba05dbb7ef3af351084ce18784cffa4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291081,
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
      "evaluated_at": 1760291081
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
  "sig": "93033f7c73da8f9a9629f310359673cd9e2b9576047000f96c5466bc9c9195bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 41500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285765, 'matching_hash': '9c2417d6ee361cba'}}}