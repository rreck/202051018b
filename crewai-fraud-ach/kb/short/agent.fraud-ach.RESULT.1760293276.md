```json
{
  "id": "160ad31c68849b59",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293276,
  "host_pid": "9e6742732c60:1",
  "hash": "75c4a9fb32403e7576188b9dfb22ab1b93ed41bb039a2a940412a201c8656637",
  "cid": "QmV175c4a9fb32403e7576188b9dfb22ab1b93ed41bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293276,
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
      "evaluated_at": 1760293276
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
  "sig": "04e38ff765840df398e5e55e1ae7782cae1c4a2d16789d07c72ff56b2c650ca6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028413829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 33262220, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '35164be796d7e820'}}}