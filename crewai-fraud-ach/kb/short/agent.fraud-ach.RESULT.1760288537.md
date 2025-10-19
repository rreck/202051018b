```json
{
  "id": "cda7d2fec67d1897",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288537,
  "host_pid": "9e6742732c60:1",
  "hash": "49821082a08c85b1175766c178b7954770988f7a4c5f12d62a5a929706560139",
  "cid": "QmV149821082a08c85b1175766c178b7954770988f7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288537,
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
      "evaluated_at": 1760288537
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
  "sig": "124143a481ac323bbf290693a85673ab23aa6755bf00ec16711b7dbdde84ae3e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031078531
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285765, 'matching_hash': '2bea5b783a868e31'}}}