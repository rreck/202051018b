```json
{
  "id": "c823eb848e26523c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286507,
  "host_pid": "9e6742732c60:1",
  "hash": "4938c9bf15ecb6df191bf3a5281f5eed55a3e6798499773c6030bffed53ccf82",
  "cid": "QmV14938c9bf15ecb6df191bf3a5281f5eed55a3e679",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286507,
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
      "evaluated_at": 1760286507
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
  "sig": "7cef853cc963c8367c190ff2dff620a049f6c114143e85321d33be5baa6c8845"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}