```json
{
  "id": "d5a2e754197f7b83",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294222,
  "host_pid": "9e6742732c60:1",
  "hash": "5ad8cd1d7a32b17f163873706ccf65c656ef0639f7a3fcf2a86668dcd4dcb75a",
  "cid": "QmV15ad8cd1d7a32b17f163873706ccf65c656ef0639",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294222,
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
      "evaluated_at": 1760294222
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
  "sig": "07d405831a735edbcfc53076ca1b764e2fda703a3a93f69a973c90bd5a693570"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 041887157928370
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 101781342, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '40835df504bb3fdd'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '041887155', 'validation_error': 'Invalid routing number checksum'}}}