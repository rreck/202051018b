```json
{
  "id": "f506a7e3d8f5229e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288698,
  "host_pid": "9e6742732c60:1",
  "hash": "374a8ef1dd153a9c43a7e75aa4cb33e609da340186149e8cdc69d45a9e37c013",
  "cid": "QmV1374a8ef1dd153a9c43a7e75aa4cb33e609da3401",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288698,
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
      "evaluated_at": 1760288698
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
  "sig": "b35ad5e7faaa555f56a4c21a36923dc6884b75878cfabbf3bf73da4fe47077c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029265266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 37076393, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285764, 'matching_hash': 'a9619dd56a360910'}}}