```json
{
  "id": "f945f60f9be02f3c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293216,
  "host_pid": "9e6742732c60:1",
  "hash": "31bd3c685e9f1bfca44f95f59fc03ca9e88f423d886f997713f57c213afb3e97",
  "cid": "QmV131bd3c685e9f1bfca44f95f59fc03ca9e88f423d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293216,
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
      "evaluated_at": 1760293216
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
  "sig": "5435656b30c6d667b8050d7de77fab9f656c6d3b4b2953a24f58d46a03240c03"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240814513
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 63354272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '8ef20234ae18fb17'}}}