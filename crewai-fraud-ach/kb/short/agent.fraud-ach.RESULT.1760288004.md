```json
{
  "id": "b55cee5e90cfba6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288004,
  "host_pid": "9e6742732c60:1",
  "hash": "91369e6b5d7fbe5fc77f3ec1a7ab166d7f6e033318ba5763cbd9530eb2c2713f",
  "cid": "QmV191369e6b5d7fbe5fc77f3ec1a7ab166d7f6e0333",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288004,
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
      "evaluated_at": 1760288004
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
  "sig": "490b16772513d1348fb975555197898accadcb580193136b4bad73dc3c8e51ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275178719
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 13115343, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285765, 'matching_hash': '267c9e50b53a1b99'}}}