```json
{
  "id": "33ef880d94ed7259",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286769,
  "host_pid": "9e6742732c60:1",
  "hash": "92f115bd728aac92c1542b69c21b8a4b444fb12332ba2642a44a654f5777efb3",
  "cid": "QmV192f115bd728aac92c1542b69c21b8a4b444fb123",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286769,
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
      "evaluated_at": 1760286769
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
  "sig": "e2ee94942fb386ccd20f078f23d868ddcdd14a3261d977c5ab9e7fecaa815932"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11456928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}