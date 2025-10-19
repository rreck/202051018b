```json
{
  "id": "1887cf95a50d91de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286875,
  "host_pid": "9e6742732c60:1",
  "hash": "5a1f111998a6a0a234aac88eb38e8db0135427bac91558d4e0757bfa50743324",
  "cid": "QmV15a1f111998a6a0a234aac88eb38e8db0135427ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286875,
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
      "evaluated_at": 1760286875
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
  "sig": "1bbe36c0546b398a4508649003e6bc932c1dcdbcb55019dec004b68ec8a4a585"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 683146203883533
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14896880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285764, 'matching_hash': '8f404d0fc37310f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '683146208', 'validation_error': 'Invalid routing number checksum'}}}