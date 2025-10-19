```json
{
  "id": "a60236dbd2657c35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293996,
  "host_pid": "9e6742732c60:1",
  "hash": "0152a265134e7f3ff67e05bed31a2b8c996d1c7c5fd42888107aa26ab2cf1027",
  "cid": "QmV10152a265134e7f3ff67e05bed31a2b8c996d1c7c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293996,
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
      "evaluated_at": 1760293996
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
  "sig": "786f64775f78327efbe3daa142523c9852e978881410bc4df5d6e1ddb7372dbb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 72878792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}