```json
{
  "id": "85de0e653953e998",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286740,
  "host_pid": "9e6742732c60:1",
  "hash": "3b8e9addb13a8563d2ddfbf005c9a46b9edb8e64ff0d930009bc9a6639d82223",
  "cid": "QmV13b8e9addb13a8563d2ddfbf005c9a46b9edb8e64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286740,
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
      "evaluated_at": 1760286740
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "378fa3023c631cf849aa06d0a125cdcbc87dcbef4f8c19eed6d13ccbf572a146"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11138680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}