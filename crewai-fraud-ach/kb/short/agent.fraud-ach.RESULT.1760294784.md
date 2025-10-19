```json
{
  "id": "f0a6e00cec789fce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294784,
  "host_pid": "9e6742732c60:1",
  "hash": "a52270f7de5f778fcf5904b684912f5c18da69123bab0178251b052927c32f9b",
  "cid": "QmV1a52270f7de5f778fcf5904b684912f5c18da6912",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294784,
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
      "evaluated_at": 1760294784
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
  "sig": "c36553ff449ea1728d23ce578820b200af2210dee1a715e1bc4c08674ba6cecb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469526930
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 27761832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285764, 'matching_hash': 'b6b808f7611ea662'}}}