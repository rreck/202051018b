```json
{
  "id": "b57be9cc6f79b09b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290501,
  "host_pid": "9e6742732c60:1",
  "hash": "fce7de7c0596fc5596f0f55ad78bc261493c3b5f69749a75c63d0d0f5cf82e13",
  "cid": "QmV1fce7de7c0596fc5596f0f55ad78bc261493c3b5f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290501,
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
      "evaluated_at": 1760290501
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
  "sig": "e9532e6da33dd1f9e0c932f46a366f4663975df862e8e4810a6b4100957c372a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025319716
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 38868072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285764, 'matching_hash': '46cae66c8ff70b91'}}}