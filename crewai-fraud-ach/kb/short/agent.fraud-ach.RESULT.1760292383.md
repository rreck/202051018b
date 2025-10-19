```json
{
  "id": "976faab450f4b18b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292383,
  "host_pid": "9e6742732c60:1",
  "hash": "f227b6367bf09798303b6dfef594761f1b67d3788ea634e2be9b95e5467c62a6",
  "cid": "QmV1f227b6367bf09798303b6dfef594761f1b67d378",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292383,
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
      "evaluated_at": 1760292383
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
  "sig": "04cb08a47ecedb4da105a7e4ed18f6e6c1f8f63bb1a1033bc293c78533bfefde"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 479377306721842
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 64021832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285764, 'matching_hash': '9b6eff4280210a62'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '479377304', 'validation_error': 'Invalid routing number checksum'}}}