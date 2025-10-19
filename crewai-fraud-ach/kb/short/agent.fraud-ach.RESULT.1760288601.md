```json
{
  "id": "bece3cdfa4c1fe1b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288601,
  "host_pid": "9e6742732c60:1",
  "hash": "5f2161eb88c43a1e2c72bb64409d38aab6f9211faa36cc8681172a0d0cc71e23",
  "cid": "QmV15f2161eb88c43a1e2c72bb64409d38aab6f9211f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288601,
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
      "evaluated_at": 1760288601
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
  "sig": "e74769bfe3ab622f0e558cc13f8f3bf0e83a029ff8ecac45a8be0bdef9e99935"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034581430
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 39740274, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285764, 'matching_hash': '1e0cfdc13a2b6c27'}}}