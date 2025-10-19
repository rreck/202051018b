```json
{
  "id": "4010b07af6a5611f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288477,
  "host_pid": "9e6742732c60:1",
  "hash": "1a22b34fad483b864b35994abe49f8c94bd0f6f49b23d511f97df83a2746c74f",
  "cid": "QmV11a22b34fad483b864b35994abe49f8c94bd0f6f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288477,
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
      "evaluated_at": 1760288477
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
  "sig": "b056ccc6c89ed6e17030a2b8da9affaf58868d0937547fdc36c5af2da1440088"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 29915312, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}