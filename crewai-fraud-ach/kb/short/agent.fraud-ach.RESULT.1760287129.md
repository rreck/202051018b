```json
{
  "id": "4056069c7ba7e583",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287129,
  "host_pid": "9e6742732c60:1",
  "hash": "8b5be780c5e6f733430c3fca89725cd2b0587a3ae819b21a79304cbd267127f1",
  "cid": "QmV18b5be780c5e6f733430c3fca89725cd2b0587a3a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287129,
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
      "evaluated_at": 1760287129
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "80092077a83558736101262cf5da99655984d7f9152f41a841a0566ea81d887c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100279970164
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285765, 'matching_hash': 'dc8a7598801f2a18'}}}k_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285763, 'matching_hash': '2df17da091128ee2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '288759214', 'validation_error': 'Invalid routing number checksum'}}}