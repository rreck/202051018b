```json
{
  "id": "8e177d59cb3431e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288427,
  "host_pid": "9e6742732c60:1",
  "hash": "570e85b8346a1b3f36e0d13de1cfddcde5ea8e1fdbd073728b37b9104d57da52",
  "cid": "QmV1570e85b8346a1b3f36e0d13de1cfddcde5ea8e1f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288427,
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
      "evaluated_at": 1760288427
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
  "sig": "3b3cf66566f9bc5f4d41d976849dcb63875aa4045860e41614096e6bb36df2d2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245084656
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 32458116, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285763, 'matching_hash': '11924a0da29b01ce'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}