```json
{
  "id": "ef36b99858ef3834",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290945,
  "host_pid": "9e6742732c60:1",
  "hash": "17ef1885738bad0ee57add23867c743ac95d7d1c7fef926f14bcf6f0b5d98c57",
  "cid": "QmV117ef1885738bad0ee57add23867c743ac95d7d1c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290945,
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
      "evaluated_at": 1760290945
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
  "sig": "c1d5c97221902ad19cb64a29204c1fd8cd35f83321f61d9957d1c7295d02d36b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276997857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 77546761, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': 'b73e9a6de72cc131'}}}