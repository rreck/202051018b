```json
{
  "id": "40a95eb532d9a2f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287611,
  "host_pid": "9e6742732c60:1",
  "hash": "6382be1895754b74b9eefdee93f07143e0bf2bf42c79c7456a635e359ae73aca",
  "cid": "QmV16382be1895754b74b9eefdee93f07143e0bf2bf4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287611,
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
      "evaluated_at": 1760287611
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
  "sig": "91f97498042a681021a3e78bdb75c2930d47640642251582788dcd51ec945e42"
}
```

Fraud detected: round_amount_pattern (score: 69)
Transaction: 031201467949832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 66000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285764, 'matching_hash': '3eb2ce6b003836d6'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}