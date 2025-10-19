```json
{
  "id": "85a9065de16b3051",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291662,
  "host_pid": "9e6742732c60:1",
  "hash": "ad55c347b577e874526ab178a31e32f851a13e3370f97df12e87e6ee351a7313",
  "cid": "QmV1ad55c347b577e874526ab178a31e32f851a13e33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291662,
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
      "evaluated_at": 1760291662
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
  "sig": "4cd82fb88e16a07a241a0aa3b189d335ea3fce1939361338718a3579b32e1191"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023633805
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 66097260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285764, 'matching_hash': 'd4295adac9eefcb9'}}}