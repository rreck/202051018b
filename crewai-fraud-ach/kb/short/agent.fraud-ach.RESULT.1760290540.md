```json
{
  "id": "3e7f693e08eb3675",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290540,
  "host_pid": "9e6742732c60:1",
  "hash": "41e7b13b8ef2ef30e2f2610a1c63bd8354a19b7443237db6204eac87cdb22bbe",
  "cid": "QmV141e7b13b8ef2ef30e2f2610a1c63bd8354a19b74",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290540,
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
      "evaluated_at": 1760290540
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
  "sig": "c0685383af03eb01c0bca1bbac2f59646fdd9a795a92ab63ca76e62404aab96f"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 542300578273472
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 38139534, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285764, 'matching_hash': '6580c6d1de434ae0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '542300570', 'validation_error': 'Invalid routing number checksum'}}}