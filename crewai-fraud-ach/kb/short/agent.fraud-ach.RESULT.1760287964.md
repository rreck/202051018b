```json
{
  "id": "a9f56f0da0ae5c3a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287964,
  "host_pid": "9e6742732c60:1",
  "hash": "d129a3dddb65e0cce0d12c02f260b178a9c2411403e321e2bb7f69d7b6651c7e",
  "cid": "QmV1d129a3dddb65e0cce0d12c02f260b178a9c24114",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287964,
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
      "evaluated_at": 1760287964
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
  "sig": "61f275b06f88fac0bff62a90c0ba9790521f9e9fdffcd375923e997a2ce5ad00"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461436182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 10506132, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285765, 'matching_hash': 'd641045bf224534b'}}}