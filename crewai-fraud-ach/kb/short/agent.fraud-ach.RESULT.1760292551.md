```json
{
  "id": "342cdace01f7fff0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292551,
  "host_pid": "9e6742732c60:1",
  "hash": "4af9010f06c47216c84f943bc005be051b0051bd078ca537c872c5b8a3dc653a",
  "cid": "QmV14af9010f06c47216c84f943bc005be051b0051bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292551,
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
      "evaluated_at": 1760292551
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
  "sig": "0faee42d6b5e26431cd88d303bcc711142e25b4b549d8823c5f065f0273a0bc1"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 498752223480159
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 78758600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': '492624c5b9a9c8c0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '498752220', 'validation_error': 'Invalid routing number checksum'}}}