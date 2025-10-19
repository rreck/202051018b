```json
{
  "id": "16e6d57b42c26867",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293375,
  "host_pid": "9e6742732c60:1",
  "hash": "2b11c159555b45873b88178a1e1c35e258feee65074e49015d8d0d9f3886ee24",
  "cid": "QmV12b11c159555b45873b88178a1e1c35e258feee65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293375,
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
      "evaluated_at": 1760293375
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
  "sig": "0510aff5e6344b2d0a13d4e353cf54d41600268f325174f0b8d9b59fb97fb0c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461577963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 94366356, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285764, 'matching_hash': '6bf1d905269d1dd3'}}}