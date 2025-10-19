```json
{
  "id": "472853ab8203977b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290640,
  "host_pid": "9e6742732c60:1",
  "hash": "3a46687e1f387eb0d6a5452ac28fab731ef3aca9bf4ea81971c9a30519e9ba95",
  "cid": "QmV13a46687e1f387eb0d6a5452ac28fab731ef3aca9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290640,
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
      "evaluated_at": 1760290640
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
  "sig": "7514a891df230f7d7f95682bbe7d01e376fb5dc302ba6db568e8b855d96f176a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 49328440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}