```json
{
  "id": "99187321a661411c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293077,
  "host_pid": "9e6742732c60:1",
  "hash": "d781e128218178da1746c481b8763cbef0fa070164b7a10df5ad24b5c4d3bb1b",
  "cid": "QmV1d781e128218178da1746c481b8763cbef0fa0701",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293077,
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
      "evaluated_at": 1760293077
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
  "sig": "14d03fff098f1d1d3029f6f1837e0b6ad55323f14bd17cf517461f167221a7cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464749166
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 75245132, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285764, 'matching_hash': '2c72b457e71ecad2'}}}