```json
{
  "id": "de804c2c499e6997",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286994,
  "host_pid": "9e6742732c60:1",
  "hash": "16fe61c7637c4521ec99195966c866ada93ea6ab0a47ff7c6a128ec064874d8e",
  "cid": "QmV116fe61c7637c4521ec99195966c866ada93ea6ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286994,
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
      "evaluated_at": 1760286994
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
  "sig": "8d6fa7aa61270c66eaf1f7a9dcad83e1673bbac7d2e7c88ec67567606227ec6c"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 635242948975660
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18907328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285765, 'matching_hash': '596a6d950333709b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '635242942', 'validation_error': 'Invalid routing number checksum'}}}