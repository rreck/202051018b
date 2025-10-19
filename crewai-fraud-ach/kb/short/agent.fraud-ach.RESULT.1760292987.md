```json
{
  "id": "0b5690157f08de00",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292987,
  "host_pid": "9e6742732c60:1",
  "hash": "2d2cc2fd4e2a90027b47fa277c3c1de67e98d585d702dc98cc6cba4af244e744",
  "cid": "QmV12d2cc2fd4e2a90027b47fa277c3c1de67e98d585",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292987,
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
      "evaluated_at": 1760292987
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
  "sig": "ab534491f6073cda10d2519f153562ae4603398b1e30c85b577bbc3c9e00b701"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468078455
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 93831177, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285764, 'matching_hash': '379f6acb9d31a698'}}}