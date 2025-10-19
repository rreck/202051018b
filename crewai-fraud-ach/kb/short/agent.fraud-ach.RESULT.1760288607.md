```json
{
  "id": "63ed34b1b52dfb43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288607,
  "host_pid": "9e6742732c60:1",
  "hash": "ad52e5c7850e0369e8cfcfa249664d223461ebe425d5b3897fe955926ebdc57d",
  "cid": "QmV1ad52e5c7850e0369e8cfcfa249664d223461ebe4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288607,
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
      "evaluated_at": 1760288607
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
  "sig": "d4a1a82d2896b6b5901f80ea2d72261ef16905890b1e1fcc20305b10dc471105"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 31188304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}