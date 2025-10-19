```json
{
  "id": "09a27ae5b54f135a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286116,
  "host_pid": "9e6742732c60:1",
  "hash": "013744041740958330f793f2e6f805c109984fc69203e229d79fc6478adb637f",
  "cid": "QmV1013744041740958330f793f2e6f805c109984fc6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286116,
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
      "evaluated_at": 1760286116
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
  "sig": "7b088009ec66e03dc5e19e34918ae39f347b084ac97642e202df5ec13e9ed60f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000026803563
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': 'cf30c88fa01e3081'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}