```json
{
  "id": "05db18394d0c9c37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290388,
  "host_pid": "9e6742732c60:1",
  "hash": "9b87b75e06d6f3a68c1372f3af7474c7371f820e85d07a5fad668672fbf5686f",
  "cid": "QmV19b87b75e06d6f3a68c1372f3af7474c7371f820e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290388,
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
      "evaluated_at": 1760290388
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
  "sig": "98d1c8f5ea8a9c154ca8bf188da28d94d36b4163605c8406dfa7ca6ea5ebda56"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464749166
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 53135188, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285764, 'matching_hash': '2c72b457e71ecad2'}}}