```json
{
  "id": "ec2cefa5a59f44c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288854,
  "host_pid": "9e6742732c60:1",
  "hash": "43aa36bd36aeb8541e596a914133f73caad6c22bb8f5ace245ab398bec326198",
  "cid": "QmV143aa36bd36aeb8541e596a914133f73caad6c22b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288854,
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
      "evaluated_at": 1760288854
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
  "sig": "5f9797c234ea17f179ceb94b2b1a88adafce1b7f91377dfba439a955b3780494"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240945799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '2868277a63cf50ca'}}}5765, 'matching_hash': '36501cb7899f5f80'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '051442869', 'validation_error': 'Invalid routing number checksum'}}}