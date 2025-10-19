```json
{
  "id": "efa894040955f096",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290826,
  "host_pid": "9e6742732c60:1",
  "hash": "1412c04264b7dae0d3ed2f8a91404a7e4d62adf6c6722d7fa14ca0a9f8c03ebd",
  "cid": "QmV11412c04264b7dae0d3ed2f8a91404a7e4d62adf6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290826,
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
      "evaluated_at": 1760290826
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
  "sig": "5b65bfdf2b7422f48ad6962c30f8bdc4d927b77bd7fc9a51a8b1f8f4d46584af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034789126
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 50518396, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760284979, 'matching_hash': '5ec025bcbfaa0fd9'}}}