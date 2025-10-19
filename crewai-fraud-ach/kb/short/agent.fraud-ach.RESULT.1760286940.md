```json
{
  "id": "1337ca8e488a6e93",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286940,
  "host_pid": "9e6742732c60:1",
  "hash": "38d507f4a416b24a5cff4b268da9dcb24072cb552b918935eaeffa24bee257d0",
  "cid": "QmV138d507f4a416b24a5cff4b268da9dcb24072cb55",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286940,
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
      "evaluated_at": 1760286940
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
  "sig": "1b184ba9b32ca2b4699ae7295a84a26df4fa61aad89f7cdf107b25ec0d48263c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009594254224
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285765, 'matching_hash': 'a2bdc2eb52125893'}}}