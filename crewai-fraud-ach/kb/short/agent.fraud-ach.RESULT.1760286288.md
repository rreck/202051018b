```json
{
  "id": "2837c5017472f657",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286288,
  "host_pid": "9e6742732c60:1",
  "hash": "a711afa2dc71deb756377237b16f1559c6d4233fec5ef8c0045470174f0dc724",
  "cid": "QmV1a711afa2dc71deb756377237b16f1559c6d4233f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286288,
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
      "evaluated_at": 1760286288
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
  "sig": "05a44069141c2b124fff0b25910016d51416566ba4bcbd6ac06af8e481854539"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 357223800655087
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285765, 'matching_hash': '6810f1ba8ee75217'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '357223803', 'validation_error': 'Invalid routing number checksum'}}}