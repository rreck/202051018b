```json
{
  "id": "a15dd272395e1dce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288987,
  "host_pid": "9e6742732c60:1",
  "hash": "35214938f1d10c6a87823a67acd9f7c6cae15e4767aeaf1524d28ea7d97545f9",
  "cid": "QmV135214938f1d10c6a87823a67acd9f7c6cae15e47",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288987,
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
      "evaluated_at": 1760288987
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
  "sig": "71930398daa677858d2f3dc98d93aeee7dd24754f8e115b707855d6f0bfb1ad3"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201463963144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 55000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285765, 'matching_hash': '4b7135c5b7384c49'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}