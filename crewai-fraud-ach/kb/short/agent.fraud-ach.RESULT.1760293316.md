```json
{
  "id": "39749079aa0ced1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293316,
  "host_pid": "9e6742732c60:1",
  "hash": "af0fca979f60f100bb39d2b383866cd566308b44d728379873c17589364bb423",
  "cid": "QmV1af0fca979f60f100bb39d2b383866cd566308b44",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293316,
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
      "evaluated_at": 1760293316
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
  "sig": "78da55925b9d8ae836cc514b8bdd152c2639a8a9414e30078079d7d0ae1cb1a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596829725
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 71380224, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '14fa64c7f7d5a53d'}}}