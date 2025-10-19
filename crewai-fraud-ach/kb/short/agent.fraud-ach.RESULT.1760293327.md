```json
{
  "id": "df1bdb497c792199",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293327,
  "host_pid": "9e6742732c60:1",
  "hash": "eca6f49ab2910b2be0639724e11e1ccc9e76b4a1cbc07eab0fe9b7881f5be1cf",
  "cid": "QmV1eca6f49ab2910b2be0639724e11e1ccc9e76b4a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293327,
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
      "evaluated_at": 1760293327
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
  "sig": "0e8c6552305ad353b3fec5b94245f4ff7f67ede9cdd2b080d5664cec96e499a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590785424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 14632488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': 'b02577e012abfee0'}}}