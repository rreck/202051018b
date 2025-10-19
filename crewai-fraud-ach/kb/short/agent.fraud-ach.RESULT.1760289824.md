```json
{
  "id": "6cf0e73425d80034",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289824,
  "host_pid": "9e6742732c60:1",
  "hash": "2affc2acc822172ccbcb05b91a491852739da81997e67d8acc1ffbf333606567",
  "cid": "QmV12affc2acc822172ccbcb05b91a491852739da819",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289824,
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
      "evaluated_at": 1760289824
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
  "sig": "e8ae4bfd09b883b5d38f63fec3d0e665739f767fe6aca318ee97052b68ff62cb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026198505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 62765734, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285764, 'matching_hash': '8ff7ad30241d2e02'}}}