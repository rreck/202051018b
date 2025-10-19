```json
{
  "id": "a0764d0e3003ddfc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293435,
  "host_pid": "9e6742732c60:1",
  "hash": "8c0fd196398d37db5f6c42153b3bca1ed7fb7822bc12ee4cf5fdc2e0249ec65d",
  "cid": "QmV18c0fd196398d37db5f6c42153b3bca1ed7fb7822",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293435,
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
      "evaluated_at": 1760293435
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
  "sig": "48e6cb58f81d92fe3bd1c4f2797753d32067165a11a442caa2e187a76c73ed5e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026725963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 44005044, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285765, 'matching_hash': '729970816697b41b'}}}