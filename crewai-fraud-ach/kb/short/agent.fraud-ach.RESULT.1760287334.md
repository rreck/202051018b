```json
{
  "id": "d2ab2ba8d3ae373d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287334,
  "host_pid": "9e6742732c60:1",
  "hash": "a7b6a8413681b6f55882ba3be7dff109b027f2edaf5a902a7990303f05264f19",
  "cid": "QmV1a7b6a8413681b6f55882ba3be7dff109b027f2ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287334,
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
      "evaluated_at": 1760287334
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
  "sig": "f46d17105c36e9b840753b3df3db7a0394d925d4879fc9cf2310f52d4ea930bf"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105152240558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 23349592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285765, 'matching_hash': '0371944fd59dbf43'}}}