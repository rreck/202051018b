```json
{
  "id": "8af8c258c0f03430",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293124,
  "host_pid": "9e6742732c60:1",
  "hash": "7924ae6baee3a2f23a02ad1671d00df7aad0c1ea1338155e3ba4a8273a91b379",
  "cid": "QmV17924ae6baee3a2f23a02ad1671d00df7aad0c1ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293124,
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
      "evaluated_at": 1760293124
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
  "sig": "789a15cc803fe5dd8eaa2e26832050f88d086c8ab09993919c557978fba9acae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274960966
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 24753120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': 'f5e3b3cd48fefc81'}}}}