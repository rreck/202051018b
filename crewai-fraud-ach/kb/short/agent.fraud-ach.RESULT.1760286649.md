```json
{
  "id": "767a8fa07f23055e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286649,
  "host_pid": "9e6742732c60:1",
  "hash": "def0450a2997188d2bb2c8cff3c863a6fe692d81882ef642ce1020da5398b620",
  "cid": "QmV1def0450a2997188d2bb2c8cff3c863a6fe692d81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286649,
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
      "evaluated_at": 1760286649
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
  "sig": "6267e6a0cec3824dfb4a54da21b8e2afc212158251aefb3733b5be0ad5ebad8e"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 589241761167275
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10035648, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285765, 'matching_hash': 'a1dced1ef969015f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '589241760', 'validation_error': 'Invalid routing number checksum'}}}