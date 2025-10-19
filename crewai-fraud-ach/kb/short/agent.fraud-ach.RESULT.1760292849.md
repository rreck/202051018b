```json
{
  "id": "2cbc3cfba0c69156",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292849,
  "host_pid": "9e6742732c60:1",
  "hash": "f07ec2f0a05209e47d362526587e8a26e519764f786ffa696fc256424a1e4475",
  "cid": "QmV1f07ec2f0a05209e47d362526587e8a26e519764f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292849,
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
      "evaluated_at": 1760292849
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
  "sig": "74363b69327ebd46d06de9523af5a1e51bfe786c191dc5007c83006be1f754e7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154440687
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 57723466, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '04c13f034fff9f4d'}}}