```json
{
  "id": "36cb1e200a180352",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287819,
  "host_pid": "9e6742732c60:1",
  "hash": "9436210bd7d956a3711d5e9e6f2afe0cec4b2579d6244cbb8cd3ea86ef932fdc",
  "cid": "QmV19436210bd7d956a3711d5e9e6f2afe0cec4b2579",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287819,
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
      "evaluated_at": 1760287819
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
  "sig": "3c1b162ace339a4ca79308162674b888e471d65cbccec7a9de898e4d6e8da486"
}
```

Fraud detected: invalid_routing (score: 92)
Transaction: 264316140004295
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 28410359, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285765, 'matching_hash': 'f346c773c62e50ad'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '264316140', 'validation_error': 'Invalid routing number checksum'}}}