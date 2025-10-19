```json
{
  "id": "4957061ae1bdf379",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290818,
  "host_pid": "9e6742732c60:1",
  "hash": "548e727aa052fde22eeea99870f8662196c0fe86e690021b3740cf023a193e01",
  "cid": "QmV1548e727aa052fde22eeea99870f8662196c0fe86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290818,
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
      "evaluated_at": 1760290818
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
  "sig": "69a7cb037c41471418bad10dd6b8a916a125f346b8b6e6f94c6fc59938160c79"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270910087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 64659520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': '020bc3c8298f3eb9'}}}