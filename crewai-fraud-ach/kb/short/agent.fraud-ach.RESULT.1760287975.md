```json
{
  "id": "8ced9da68947683e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287975,
  "host_pid": "9e6742732c60:1",
  "hash": "31be5ba6e9fc819b7846ee8e20e2769b1cf93d8294397db1332224ccb2bac359",
  "cid": "QmV131be5ba6e9fc819b7846ee8e20e2769b1cf93d82",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287975,
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
      "evaluated_at": 1760287975
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
  "sig": "26fb00936c642943c5337ca9e293e1e7d953a1806ce1b6c64a8fefe79e5c8138"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 24823344, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}