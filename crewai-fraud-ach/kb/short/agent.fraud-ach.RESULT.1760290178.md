```json
{
  "id": "f46a060d1599c163",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290178,
  "host_pid": "9e6742732c60:1",
  "hash": "6be8208661dc04f915269ea3ce85bc18efd9e54438e9f89e5539405367c0cddd",
  "cid": "QmV16be8208661dc04f915269ea3ce85bc18efd9e544",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290178,
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
      "evaluated_at": 1760290178
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
  "sig": "575a0f52cd8f103ae60e26f911e37a2e1d9592772ddaa5842dbb4c633e639468"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 45509464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}