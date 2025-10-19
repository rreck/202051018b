```json
{
  "id": "c06e63b31fd43bae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287044,
  "host_pid": "9e6742732c60:1",
  "hash": "023aa33fd86a48cb2edd6b7767fc5994ece6fe0772c5c30cff764692971de5ef",
  "cid": "QmV1023aa33fd86a48cb2edd6b7767fc5994ece6fe07",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287044,
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
      "evaluated_at": 1760287044
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
  "sig": "f42942966885d81150d68748f3ec21b9d60d5db404f1e5bdb3702ef975bc5208"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 870312149939109
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18356622, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285765, 'matching_hash': '2dbf2bb6cc4c52b4'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '870312145', 'validation_error': 'Invalid routing number checksum'}}}