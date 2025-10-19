```json
{
  "id": "ff87560bbdc11323",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286620,
  "host_pid": "9e6742732c60:1",
  "hash": "fa3bdcb07928fac93d14a3451643ef116dd791926973b2ee461005bb34f8a17c",
  "cid": "QmV1fa3bdcb07928fac93d14a3451643ef116dd79192",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286620,
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
      "evaluated_at": 1760286620
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "712383592bc02bceef68e8bea80a677e6160581b8de532da51ec9f8dada92b2a"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 026009597287610
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 31000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285765, 'matching_hash': 'd127b5f232f25796'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}