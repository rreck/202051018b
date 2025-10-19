```json
{
  "id": "cbf9b5a81b92f268",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291113,
  "host_pid": "9e6742732c60:1",
  "hash": "2981b3a01013d3f87fc69680f216944a7216988376c525bbee9ba8335f164d98",
  "cid": "QmV12981b3a01013d3f87fc69680f216944a72169883",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291113,
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
      "evaluated_at": 1760291113
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
  "sig": "e72754647d704ce722d4fc4722d0ab6033a8e1f8d30d5a2f58ac0edb6c9abacd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460464182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 17640043, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285765, 'matching_hash': '97f231b14306ced8'}}}