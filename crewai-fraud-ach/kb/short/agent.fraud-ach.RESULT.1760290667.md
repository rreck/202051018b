```json
{
  "id": "e311a91038d2e304",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290667,
  "host_pid": "9e6742732c60:1",
  "hash": "0b4a41754fbe6af3286649553b6fbedb3cc8e2bd7297a8543ac31d048835b8a5",
  "cid": "QmV10b4a41754fbe6af3286649553b6fbedb3cc8e2bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290667,
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
      "evaluated_at": 1760290667
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
  "sig": "0a98bd78e2efe07fc79b4e3f91649992d41ac3ec5e7c2d01c30e1e334e693d2d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023759733
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 35950824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285765, 'matching_hash': 'cdd972b8484ef71b'}}}}