```json
{
  "id": "d15e543eb2279c8a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291757,
  "host_pid": "9e6742732c60:1",
  "hash": "7ced1dbb04699198024f4f350bac37872ce74daf4a0d3038b408766d68ee7728",
  "cid": "QmV17ced1dbb04699198024f4f350bac37872ce74daf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291757,
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
      "evaluated_at": 1760291757
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
  "sig": "e3834ff41e52ffbf251513a04b25d3860c46461d38c7994de0a1f419bccefbb8"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 683146203883533
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 67780804, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285764, 'matching_hash': '8f404d0fc37310f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '683146208', 'validation_error': 'Invalid routing number checksum'}}}