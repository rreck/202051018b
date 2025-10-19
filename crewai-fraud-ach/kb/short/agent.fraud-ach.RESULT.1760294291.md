```json
{
  "id": "ae13a57a04f1b242",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294291,
  "host_pid": "9e6742732c60:1",
  "hash": "bc7af81b08499259964b285b9bd01cf4b4868a029426befdd16874cab2b76fcc",
  "cid": "QmV1bc7af81b08499259964b285b9bd01cf4b4868a02",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294291,
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
      "evaluated_at": 1760294291
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
  "sig": "7509ed6540139b39333ab65aaee864494f4c0f8679fda56489ab1eecf493ee54"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464946217
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 311, 'threshold': 50, 'total_amount': 105846673, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 310, 'first_seen': 1760284979, 'matching_hash': '76eefa6b67e55304'}}}