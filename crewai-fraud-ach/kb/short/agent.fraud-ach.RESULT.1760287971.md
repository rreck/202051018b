```json
{
  "id": "8e7c3b68c1827dc9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287971,
  "host_pid": "9e6742732c60:1",
  "hash": "42e752c6a1bb49ce032b06c5eb2ca0defd2cfdda9322be9ba35a668b39bf9c0d",
  "cid": "QmV142e752c6a1bb49ce032b06c5eb2ca0defd2cfdda",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287971,
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
      "evaluated_at": 1760287971
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
  "sig": "56db3f31869d910818811aa616bc9cf03ebf1b153e698940119745b7e14ed31b"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 845955323982908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 28154412, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285765, 'matching_hash': '603efe89834eadf7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '845955329', 'validation_error': 'Invalid routing number checksum'}}}