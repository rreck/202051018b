```json
{
  "id": "d8afe656fac1de71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292221,
  "host_pid": "9e6742732c60:1",
  "hash": "6e0871b191350e9da0d9fc4bbeea654a2bff2bbe8c05a18a25151ab1a6144268",
  "cid": "QmV16e0871b191350e9da0d9fc4bbeea654a2bff2bbe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292221,
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
      "evaluated_at": 1760292221
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
  "sig": "9a87023ae0cef6d9fb3707b729dcbdbfcd048d870994169bb94ee12379b60dd9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025560621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 52426520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '1e88fa5a655ec1c9'}}}