```json
{
  "id": "1aacc1b70ebe6a76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290524,
  "host_pid": "9e6742732c60:1",
  "hash": "e71225ca8f306e42bc8276891dd99bc4ae46b8df2c225628a9fd1bffc5642a34",
  "cid": "QmV1e71225ca8f306e42bc8276891dd99bc4ae46b8df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290524,
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
      "evaluated_at": 1760290524
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
  "sig": "6ec08e628b4aa0c3c2d5d1885759c688ccd1ae7483179581a7d5afeaf8832706"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 48373696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}