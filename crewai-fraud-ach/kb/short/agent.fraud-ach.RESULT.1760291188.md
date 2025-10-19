```json
{
  "id": "f9bac85e923b3b9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291188,
  "host_pid": "9e6742732c60:1",
  "hash": "3d7ae23e18d9c94ecd44a52d5d2d2f2e728fd91950605506d34653d0b7c1ca56",
  "cid": "QmV13d7ae23e18d9c94ecd44a52d5d2d2f2e728fd919",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291188,
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
      "evaluated_at": 1760291188
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
  "sig": "bcaf73b2df9f3613e7b00a7a2a774c8da92f15ad85e7a57b1914ec5d94afcbde"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030478037
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 36446540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': 'a92b61c306bd8c34'}}}