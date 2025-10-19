```json
{
  "id": "87e9b503cdadf9e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290131,
  "host_pid": "9e6742732c60:1",
  "hash": "698cff6c584ae24af02bbd52393b207d50dc12936e1fcd14d82a7d9a563ced9a",
  "cid": "QmV1698cff6c584ae24af02bbd52393b207d50dc1293",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290131,
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
      "evaluated_at": 1760290131
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
  "sig": "a915195e71ecdedd82950c9bed04c040fbf4b3a9d26397ab0a2c9661329075ce"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201463431091
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 71000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': 'c719f059714014d6'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}