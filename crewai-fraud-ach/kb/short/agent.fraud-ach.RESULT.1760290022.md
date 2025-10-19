```json
{
  "id": "b84fcade70acd4ff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290022,
  "host_pid": "9e6742732c60:1",
  "hash": "a89d155f3d68e7bdf8f31f3eb25399e93fbb4b927680074eda3232f03e5a8d78",
  "cid": "QmV1a89d155f3d68e7bdf8f31f3eb25399e93fbb4b92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290022,
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
      "evaluated_at": 1760290022
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
  "sig": "40a958bb623386e3a72f3ed44dbbc001f7502889e0ead79b5cb255a78110f69b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039498282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 69255638, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285765, 'matching_hash': 'dad018b424b66512'}}}