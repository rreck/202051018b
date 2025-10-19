```json
{
  "id": "6ead89ebaded91c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294788,
  "host_pid": "9e6742732c60:1",
  "hash": "75ce81098e3fdda501d46c124ce25b58d7b4a978b947fbef1c21f8836c7f9d64",
  "cid": "QmV175ce81098e3fdda501d46c124ce25b58d7b4a978",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294788,
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
      "evaluated_at": 1760294788
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
  "sig": "4fb522f8d40ac513d23ee835fd6add2ad7eab418d534ee7f016657454565f6a7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467961793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 16349708, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': '7ef856857e97207f'}}}