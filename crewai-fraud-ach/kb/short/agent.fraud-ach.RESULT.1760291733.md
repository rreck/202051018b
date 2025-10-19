```json
{
  "id": "2076e18ca3105125",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291733,
  "host_pid": "9e6742732c60:1",
  "hash": "23cd62224dc83e3c089b2e32aabe18bae39a38db52321d28f67575d19e0a166a",
  "cid": "QmV123cd62224dc83e3c089b2e32aabe18bae39a38db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291733,
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
      "evaluated_at": 1760291733
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
  "sig": "4040c2d0d387555a4703930b9a193d39504a6b9a02b5b43d395c0c844278feba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274159227
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 22827168, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': 'c6403d45da933f2b'}}}