```json
{
  "id": "b622544a64d11ff6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289713,
  "host_pid": "9e6742732c60:1",
  "hash": "780aebc788424a6591fb5cb3cc9eea1753630ec50ad1d858bc24741d3f116ee7",
  "cid": "QmV1780aebc788424a6591fb5cb3cc9eea1753630ec5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289713,
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
      "evaluated_at": 1760289713
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
  "sig": "364f3b17488cf5956bff87bd38dfffd553913536ba0c81c7767bdbc045a4dd61"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025664709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 13486057, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285764, 'matching_hash': '5cc83e27ca9ca801'}}}