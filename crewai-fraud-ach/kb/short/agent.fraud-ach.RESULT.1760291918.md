```json
{
  "id": "ca629842ea35eb65",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291918,
  "host_pid": "9e6742732c60:1",
  "hash": "8fc910304888c29fbf49a98fe5513731e05aa037cd12cad73ea4450178813f1d",
  "cid": "QmV18fc910304888c29fbf49a98fe5513731e05aa037",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291918,
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
      "evaluated_at": 1760291918
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
  "sig": "fd53ea6bbff452d049cb297dcf6e78399fd152206cb522264fb5a7f92a1cb5b5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271088524
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 54642522, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': '9bd457f641df29ee'}}}