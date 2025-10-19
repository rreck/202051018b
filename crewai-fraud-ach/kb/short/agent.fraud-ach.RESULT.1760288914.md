```json
{
  "id": "155bcac29f27b0d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288914,
  "host_pid": "9e6742732c60:1",
  "hash": "f669233485d32628a034b8082fb4caeedfd1571d899ad1d573732a90a52f1a64",
  "cid": "QmV1f669233485d32628a034b8082fb4caeedfd1571d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288914,
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
      "evaluated_at": 1760288914
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
  "sig": "39cac3a183e1181244338da144c19a15732c822934ce86226d7587e536be615c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278947252
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 23684508, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285763, 'matching_hash': 'c008d048aedbdb99'}}}