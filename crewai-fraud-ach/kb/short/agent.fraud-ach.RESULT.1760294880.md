```json
{
  "id": "ce88f72771875b33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294880,
  "host_pid": "9e6742732c60:1",
  "hash": "4f5a8aa3f33f85dc245c4f4f948880370d726be5c9f0d553c41dc3a09f543c6b",
  "cid": "QmV14f5a8aa3f33f85dc245c4f4f948880370d726be5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294880,
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
      "evaluated_at": 1760294880
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
  "sig": "79090e9226a883f10a3139138a8c99ce136e359815ac57630b4586d9f4cc0818"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029233033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 102147564, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': 'f6bf3c76ea3935d9'}}}