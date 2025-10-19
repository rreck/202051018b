```json
{
  "id": "d807423752be5ccc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290243,
  "host_pid": "9e6742732c60:1",
  "hash": "5d7f4b649a368cfc886d37996ec99a39eaf9e6e5a10c1a13a38d3d804599fe9d",
  "cid": "QmV15d7f4b649a368cfc886d37996ec99a39eaf9e6e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290243,
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
      "evaluated_at": 1760290243
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
  "sig": "f2fc098b6e161f2ff481f33cfdab6df21925a3034800e645b8e47ef139aad8a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155104424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 41712440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': 'b81635ada84cf521'}}}