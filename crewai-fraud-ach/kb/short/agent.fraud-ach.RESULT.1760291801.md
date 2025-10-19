```json
{
  "id": "c91ee45599a652cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291801,
  "host_pid": "9e6742732c60:1",
  "hash": "81b138568374ec7246a6411764309c87b6e4a81590b3ae94bedaaf894106349c",
  "cid": "QmV181b138568374ec7246a6411764309c87b6e4a815",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291801,
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
      "evaluated_at": 1760291801
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
  "sig": "13e32f6385b1893fe37087e4ad0d00ffd85f9d89cfdd5d59ce1104f39d242d9c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 160455148414817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 66429915, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285764, 'matching_hash': 'c57b46b00801b500'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '160455141', 'validation_error': 'Invalid routing number checksum'}}}