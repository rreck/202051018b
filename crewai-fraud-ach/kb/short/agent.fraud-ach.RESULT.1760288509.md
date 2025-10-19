```json
{
  "id": "8d5a6d0c29bccb59",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288509,
  "host_pid": "9e6742732c60:1",
  "hash": "110b49c1e08f99f9f4f1b14a4dcb1d0c5e8b16d14b0829dd5d074d52a6bb8e22",
  "cid": "QmV1110b49c1e08f99f9f4f1b14a4dcb1d0c5e8b16d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288509,
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
      "evaluated_at": 1760288509
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
  "sig": "b0385fb7ca835dfdd8c735cc801c5b1593184254f7cb8382b48c3f8e8b632881"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 30233560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}