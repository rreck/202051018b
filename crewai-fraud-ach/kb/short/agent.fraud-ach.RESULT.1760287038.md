```json
{
  "id": "02858a1afeaa5593",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287038,
  "host_pid": "9e6742732c60:1",
  "hash": "d854d73d8fe1cc27d2b714a42d48e87d2d35919155388711c406e79c7a06d942",
  "cid": "QmV1d854d73d8fe1cc27d2b714a42d48e87d2d359191",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287038,
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
      "evaluated_at": 1760287038
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
  "sig": "8035c4b24ffb49d0696ad2d208ac35cc538ecd489719c611bf93460b6f5e7d78"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 646437634699290
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20605792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285763, 'matching_hash': 'd218c468aa26fc36'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '646437635', 'validation_error': 'Invalid routing number checksum'}}}