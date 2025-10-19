```json
{
  "id": "1a237a53db125106",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289321,
  "host_pid": "9e6742732c60:1",
  "hash": "81678149b9bc4c683d67bd7495a5a8ab72f199fd33d8c3497db63aab0228bdc5",
  "cid": "QmV181678149b9bc4c683d67bd7495a5a8ab72f199fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289321,
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
      "evaluated_at": 1760289321
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
  "sig": "05bf6ff08502bda96295ff620da2e0515420479261ba988fa7cb605ae1a7d301"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244096993316032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 31183680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285763, 'matching_hash': 'b69a4a680810c6df'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244096997', 'validation_error': 'Invalid routing number checksum'}}}