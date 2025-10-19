```json
{
  "id": "2a065693e404cfc3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285841,
  "host_pid": "9e6742732c60:1",
  "hash": "172997fbe93332913ae77540d2cba226ccfb62f9eee2cdad01656166b7084457",
  "cid": "QmV1172997fbe93332913ae77540d2cba226ccfb62f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285841,
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
      "evaluated_at": 1760285841
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "30b69a8e048a2fa6b97e0364590ebfbd1a5dfca3fb8a417295a8747452fa777d"
}
```

Fraud detected: round_amount_pattern (score: 62)
Transaction: 063100273161862
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285763, 'matching_hash': '7792cb8eb05ccf8f'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}