```json
{
  "id": "6d454119efd9bdfd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293273,
  "host_pid": "9e6742732c60:1",
  "hash": "1de2aec612090ef55086052cc47b8ffe100ab9876507a747368c666f858ddeeb",
  "cid": "QmV11de2aec612090ef55086052cc47b8ffe100ab987",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293273,
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
      "evaluated_at": 1760293273
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
  "sig": "e7dfaf6a95241b27f9d5e7ace6edaeb36a672c21f74110a312ffa7d07dcc3edb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020376030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 81303110, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '92ff62b724ca331a'}}}