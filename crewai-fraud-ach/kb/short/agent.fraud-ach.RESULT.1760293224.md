```json
{
  "id": "4d65062e0b2a0794",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293224,
  "host_pid": "9e6742732c60:1",
  "hash": "62fa9e9fc100993ba7e7e58b6c22100b6b07789ee9857eee057c3d34dcfbb9f1",
  "cid": "QmV162fa9e9fc100993ba7e7e58b6c22100b6b07789e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293224,
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
      "evaluated_at": 1760293224
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
  "sig": "0e35c3faaddc5a97f55be43262aa5aa98538d3ae7c814ba4ce18353eb95c0338"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464866805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 82526746, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285764, 'matching_hash': '8f846e2074b125b7'}}}