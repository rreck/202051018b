```json
{
  "id": "af98e6ba1d67390e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288000,
  "host_pid": "9e6742732c60:1",
  "hash": "c9afe5dad3b1356e9193c3fa11fe8dc1a72450948a1d7d7904c5c0382d13d09d",
  "cid": "QmV1c9afe5dad3b1356e9193c3fa11fe8dc1a7245094",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288000,
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
      "evaluated_at": 1760288000
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
  "sig": "fb9d6768d8316e2424fdb4750d21dbbf04d9096b7b5e90197669a42cea7b98b4"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 264316140004295
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 30745457, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285765, 'matching_hash': 'f346c773c62e50ad'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '264316140', 'validation_error': 'Invalid routing number checksum'}}}