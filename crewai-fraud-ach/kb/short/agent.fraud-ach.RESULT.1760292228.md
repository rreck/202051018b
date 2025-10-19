```json
{
  "id": "001e04642819ec7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292228,
  "host_pid": "9e6742732c60:1",
  "hash": "5c4c90f5f1da4ab391f7e30eb776385bc58b0d33d56164d01211d9e5ffe464fc",
  "cid": "QmV15c4c90f5f1da4ab391f7e30eb776385bc58b0d33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292228,
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
      "evaluated_at": 1760292228
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
  "sig": "9bb6e5dca41b57bcd8407632206293f8f9cfe6092d373eb56cc1b22868285517"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036907843
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 59492636, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '5c57e03938e1b0ed'}}}