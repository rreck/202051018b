```json
{
  "id": "8904c00e2ab6270a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286877,
  "host_pid": "9e6742732c60:1",
  "hash": "d525f0d6034b977b2288588f4925d408f8cc3c5b0d08b795ca1bd732fcd86dd9",
  "cid": "QmV1d525f0d6034b977b2288588f4925d408f8cc3c5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286877,
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
      "evaluated_at": 1760286877
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
  "sig": "dcb5e144d93ec6c52fcd1e57be270808fe678cc36f99ca4832191f4332b1fa94"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 264316140004295
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15567320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285765, 'matching_hash': 'f346c773c62e50ad'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '264316140', 'validation_error': 'Invalid routing number checksum'}}}