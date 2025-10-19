```json
{
  "id": "5600364edb35372e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288092,
  "host_pid": "9e6742732c60:1",
  "hash": "cdb1305b6ad7e28466ddfb0cc52fee0f333e8092f66b77b403d9f854d09be3b0",
  "cid": "QmV1cdb1305b6ad7e28466ddfb0cc52fee0f333e8092",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288092,
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
      "evaluated_at": 1760288092
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "d56f8ebeda807fd18b701bb9f71ceb33b552c62271c6e3a975c453c390674505"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 130120308000996
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 20109188, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285765, 'matching_hash': 'd5206edc25c84cce'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '130120307', 'validation_error': 'Invalid routing number checksum'}}}