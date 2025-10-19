```json
{
  "id": "5a283e5d6c44ea4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287610,
  "host_pid": "9e6742732c60:1",
  "hash": "18377a7bbdbaf3589d28121dcf2b2ceb7f4adac3a06189219fcbd6294498d77e",
  "cid": "QmV118377a7bbdbaf3589d28121dcf2b2ceb7f4adac3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287610,
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
      "evaluated_at": 1760287610
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
  "sig": "3e9c43c24718289d9b8f4915831bc73c0d618a7311a331e059724974db235afc"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 026009591362197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 26575824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285763, 'matching_hash': 'b2660329f17701b7'}}}